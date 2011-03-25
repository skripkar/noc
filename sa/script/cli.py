# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## CLI FSM
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import re
import Queue
## NOC modules
from noc.lib.fsm import StreamFSM
from noc.sa.script.exception import *
from noc.lib.text import replace_re_group

##
## CLI FSM
##
class CLI(StreamFSM):
    FSM_NAME="CLI"
    DEFAULT_STATE="START"
    STATES={
        "START": {
            "USERNAME"            : "USERNAME",
            "PASSWORD"            : "PASSWORD",
            "UNPRIVELEGED_PROMPT" : "UNPRIVELEGED_PROMPT",
            "PROMPT"              : "PROMPT",
            "PAGER"               : "START",
        },
        "USERNAME": {
            "USERNAME"            : "FAILURE",
            "PASSWORD"            : "PASSWORD",
            "UNPRIVELEGED_PROMPT" : "UNPRIVELEGED_PROMPT",
            "PROMPT"              : "PROMPT"
        },
        "PASSWORD": {
            "USERNAME"            : "FAILURE",
            "PASSWORD"            : "FAILURE",
            "UNPRIVELEGED_PROMPT" : "UNPRIVELEGED_PROMPT",
            "PROMPT"              : "PROMPT",
            "PAGER"               : "PASSWORD",
        },
        "SUPER_USERNAME" : {
            "USERNAME"            : "FAILURE",
            "UNPRIVELEGED_PROMPT" : "FAILURE",
            "PASSWORD"            : "SUPER_PASSWORD",
            "PROMPT"              : "PROMPT",
            "PAGER"               : "SUPER_USERNAME"
        },
        "SUPER_PASSWORD" : {
            "UNPRIVELEGED_PROMPT" : "FAILURE",
            "USERNAME"            : "FAILURE",
            "PASSWORD"            : "FAILURE",
            "PROMPT"              : "PROMPT",
            "PAGER"               : "SUPER_PASSWORD"
        },
        "UNPRIVELEGED_PROMPT": {
            "USERNAME"            : "SUPER_USERNAME",
            "PASSWORD"            : "SUPER_PASSWORD",
            "PROMPT"              : "PROMPT",
        },
        "PROMPT": {
            "PROMPT"      : "PROMPT",
            "PAGER"       : "PROMPT",
            "CLOSE"       : "CLOSED",
        },
        "FAILURE":{
            "FAILURE"     : "FAILURE",
        },
        "CLOSED":{},
    }
    MATCH_TAIL=256 # Analyze last 256 characters only
    
    ##
    ## CLI constructor
    ##
    def __init__(self, profile, access_profile):
        self.profile=profile
        self.access_profile=access_profile
        self.queue=Queue.Queue()
        self.is_ready=False
        self.collected_data=""
        self.submitted_data=[]
        self.submit_lines_limit=None
        self.motd="" # Message of the day storage
        self.pattern_prompt=None # Set when entering PROMPT state
        if isinstance(self.profile.pattern_more, basestring):
            self.more_patterns=[self.profile.pattern_more]
            self.more_commands=[self.profile.command_more]
        else:
            # .more_patterns is a list of (pattern, command)
            self.more_patterns=[x[0] for x in self.profile.pattern_more]
            self.more_commands=[x[1] for x in self.profile.pattern_more]
        # Merge pager patterns
        self.pager_patterns="|".join([r"(%s)"%p for p in self.more_patterns])
        super(CLI,self).__init__(async_throttle=100000) # Switch to asynchronous check after 100K of input
    
    ##
    ## Override Socket.on_read to feed the data to FSM
    ##
    def on_read(self, data):
        self.debug("on_read: %s"%repr(data))
        # Wipe out rogue chars
        if self.profile.rogue_chars:
            for rc in self.profile.rogue_chars:
                try:
                    data=rc.sub("", data) # rc is compiled regular expression
                except AttributeError:
                    data=data.replace(rc, "") # rc is a string
        # Feed cleaned data to FSM and flush all pending submitted data
        self.feed(data, cleanup=self.profile.cleaned_input)
        self.__flush_submitted_data()
    
    ##
    ## Feed pending submitted data
    ##
    def __flush_submitted_data(self):
        if self.submitted_data:
            self.debug("%d lines to submit"%len(self.submitted_data))
            sd="\n".join(self.submitted_data[:self.submit_lines_limit])+"\n"
            self.submitted_data=self.submitted_data[self.submit_lines_limit:]
            self.write(sd)
    
    ##
    ## Submit command to CLI
    ##
    def submit(self, msg, command_submit=None, bulk_lines=None):
        self.debug("submit(%s,bulk_lines=%s)"%(repr(msg), bulk_lines))
        self.submit_lines_limit=bulk_lines
        if bulk_lines:
            self.submitted_data=msg.splitlines()
            self.__flush_submitted_data()
        else:
            self.write(msg+(self.profile.command_submit if command_submit is None else command_submit))
    
    ##
    ## Entering START state
    ##
    def on_START_enter(self):
        # username/password match
        p=[
            (self.profile.pattern_username, "USERNAME"),
            (self.profile.pattern_password, "PASSWORD"),
        ]
        # Match unpriveleged prompt when given
        if self.profile.pattern_unpriveleged_prompt:
            p+=[(self.profile.pattern_unpriveleged_prompt, "UNPRIVELEGED_PROMPT")]
        # Match priveleged prompt when given
        p+=[(self.profile.pattern_prompt, "PROMPT")]
        # Match pager
        p+=[(self.pager_patterns, "PAGER")]
        self.set_patterns(p)
    
    ##
    ## Entering USERNAME state
    ##
    def on_USERNAME_enter(self):
        self.motd="" # Reset MoTD
        self.set_patterns([
            (self.profile.pattern_password, "PASSWORD"),
            (self.profile.pattern_prompt,   "PROMPT"),
        ])
        self.submit(self.access_profile.user)
    
    ##
    ## Entering PASSWORD state
    ##
    def on_PASSWORD_enter(self):
        self.motd="" # Reset MoTD
        p=[]
        if self.profile.pattern_unpriveleged_prompt:
            p+=[(self.profile.pattern_unpriveleged_prompt,"UNPRIVELEGED_PROMPT")]
        p+=[
            (self.profile.pattern_prompt,   "PROMPT"),
            (self.profile.pattern_username, "USERNAME"),
            (self.profile.pattern_password, "PASSWORD")
            ]
        p+=[(self.pager_patterns, "PAGER")]
        self.set_patterns(p)
        self.submit(self.access_profile.password)
    
    ##
    ## Entering UNPRIVELEGED PROMPT state
    ##
    def on_UNPRIVELEGED_PROMPT_enter(self):
        self.set_patterns([
            (self.profile.pattern_username, "USERNAME"),
            (self.profile.pattern_prompt,   "PROMPT"),
            (self.profile.pattern_password, "PASSWORD")
        ])
        self.submit(self.profile.command_super)
    
    ##
    ## Entering SUPER USERNAME state
    ##
    def on_SUPER_USERNAME_enter(self):
        self.set_patterns([
            (self.profile.pattern_username, "USERNAME"),
            (self.profile.pattern_prompt,   "PROMPT"),
            (self.profile.pattern_password, "PASSWORD"),
            (self.pager_patterns,"PAGER")
        ])
        self.submit(self.access_profile.user)
    
    ##
    ## Entering SUPER PASSWORD state
    ##
    def on_SUPER_PASSWORD_enter(self):
        self.set_patterns([
            (self.profile.pattern_prompt,   "PROMPT"),
            (self.profile.pattern_password, "PASSWORD"),
            (self.pager_patterns,           "PAGER")
        ])
        sp=self.access_profile.super_password
        if not sp:
            sp=""
        self.submit(sp)
    
    ##
    ## Entering PROMPT state
    ##
    def on_PROMPT_enter(self):
        self.debug("on_PROMPT_enter")
        if not self.is_ready:
            self.pattern_prompt=self.profile.pattern_prompt
            # Refine adaprive pattern prompt
            for k,v in self.match.groupdict().items():
                v=re.escape(v)
                self.pattern_prompt=replace_re_group(self.pattern_prompt, "(?P<%s>"%k,v)
                self.pattern_prompt=replace_re_group(self.pattern_prompt, "(?P=%s"%k,v)
            self.debug("Using prompt pattern: %s"%self.pattern_prompt)
            self.queue.put(None) # Signal provider passing into PROMPT state
            self.is_ready=True
        p=[
            (self.pattern_prompt, "PROMPT"),
            (self.pager_patterns, "PAGER"),
            ]
        self.set_patterns(p)
    
    ##
    ## Collect data when entering PROMPT state
    ##
    def on_PROMPT_match(self,data,match):
        # Fall back to synchronous parsing
        self.reset_async_check()
        if match.re.pattern in self.pager_patterns:
            # Collect data before pager
            self.collected_data+=data
        elif match.re.pattern==self.pattern_prompt:
            # Submit data
            self.queue.put(self.collected_data+data)
            self.collected_data=""
    
    ##
    ## Send appropriative command to prompt
    ##
    def on_PROMPT_PAGER(self):
        pg=self.match.group(0)
        for p,c in zip(self.more_patterns, self.more_commands):
            if re.search(p,pg,re.DOTALL|re.MULTILINE):
                self.write(c)
                return
        raise InvalidPagerPattern(pg)
    
    on_START_PAGER=on_PROMPT_PAGER
    on_PASSWORD_PAGER=on_PROMPT_PAGER
    
    ##
    ## Entering FAILURE state
    ##
    def on_FAILURE_enter(self):
        self.set_patterns([])
        if not self.is_ready:
            self.queue.put(None) # Signal status upodate
        self.queue.put(LoginError(self.motd))
    
    ##
    ## Save MoTD on start
    ##
    def on_START_match(self, data, match):
        self.motd+=data
    
    on_USERNAME_match=on_START_match
    on_PASSWORD_match=on_START_match
