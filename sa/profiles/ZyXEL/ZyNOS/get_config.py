import noc.sa.script

class Script(noc.sa.script.Script):
    name="Zyxel.ZyNOS.get_config"
    def execute(self):
        config=self.cli("show running-config")
        return self.cleaned_config(config)
