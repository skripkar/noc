#!/usr/bin/python2.4
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
_ERRORCODE = descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='sae.ErrorCode',
  filename='ErrorCode',
  values=[
    descriptor.EnumValueDescriptor(
      name='ERR_OK', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INTERNAL', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_METHOD', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_TRANSACTION', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_TRANSACTION_EXISTS', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_UNKNOWN_ACTIVATOR', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_PROFILE', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_SCHEME', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_UNKNOWN_EVENT_SOURCE', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_AUTH_FAILED', index=9, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_AUTH_REQUIRED', index=10, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_UPGRADE', index=11, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_OVERLOAD', index=12, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_INVALID_SCRIPT', index=13, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_SCRIPT_EXCEPTION', index=14, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERR_ACTIVATOR_NOT_AVAILABLE', index=15, number=15,
      options=None,
      type=None),
  ],
  options=None,
)


_ACCESSSCHEME = descriptor.EnumDescriptor(
  name='AccessScheme',
  full_name='sae.AccessScheme',
  filename='AccessScheme',
  values=[
    descriptor.EnumValueDescriptor(
      name='TELNET', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SSH', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='HTTP', index=2, number=2,
      options=None,
      type=None),
  ],
  options=None,
)


ERR_OK = 0
ERR_INTERNAL = 1
ERR_INVALID_METHOD = 2
ERR_INVALID_TRANSACTION = 3
ERR_TRANSACTION_EXISTS = 4
ERR_UNKNOWN_ACTIVATOR = 5
ERR_INVALID_PROFILE = 6
ERR_INVALID_SCHEME = 7
ERR_UNKNOWN_EVENT_SOURCE = 8
ERR_AUTH_FAILED = 9
ERR_AUTH_REQUIRED = 10
ERR_INVALID_UPGRADE = 11
ERR_OVERLOAD = 12
ERR_INVALID_SCRIPT = 13
ERR_SCRIPT_EXCEPTION = 14
ERR_ACTIVATOR_NOT_AVAILABLE = 15
TELNET = 0
SSH = 1
HTTP = 2



_MESSAGE = descriptor.Descriptor(
  name='Message',
  full_name='sae.Message',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='sae.Message.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request', full_name='sae.Message.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response', full_name='sae.Message.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error', full_name='sae.Message.error', index=3,
      number=4, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='sae.Request',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='method', full_name='sae.Request.method', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='serialized_request', full_name='sae.Request.serialized_request', index=1,
      number=2, type=12, cpp_type=9, label=2,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='sae.Response',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='serialized_response', full_name='sae.Response.serialized_response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ERROR = descriptor.Descriptor(
  name='Error',
  full_name='sae.Error',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='sae.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='sae.Error.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ACCESSPROFILE = descriptor.Descriptor(
  name='AccessProfile',
  full_name='sae.AccessProfile',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='profile', full_name='sae.AccessProfile.profile', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scheme', full_name='sae.AccessProfile.scheme', index=1,
      number=2, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address', full_name='sae.AccessProfile.address', index=2,
      number=3, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='port', full_name='sae.AccessProfile.port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='sae.AccessProfile.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='sae.AccessProfile.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='super_password', full_name='sae.AccessProfile.super_password', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='path', full_name='sae.AccessProfile.path', index=7,
      number=8, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='snmp_ro', full_name='sae.AccessProfile.snmp_ro', index=8,
      number=9, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='snmp_rw', full_name='sae.AccessProfile.snmp_rw', index=9,
      number=10, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PINGREQUEST = descriptor.Descriptor(
  name='PingRequest',
  full_name='sae.PingRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PINGRESPONSE = descriptor.Descriptor(
  name='PingResponse',
  full_name='sae.PingResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_REGISTERREQUEST = descriptor.Descriptor(
  name='RegisterRequest',
  full_name='sae.RegisterRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='sae.RegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_REGISTERRESPONSE = descriptor.Descriptor(
  name='RegisterResponse',
  full_name='sae.RegisterResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nonce', full_name='sae.RegisterResponse.nonce', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_AUTHREQUEST = descriptor.Descriptor(
  name='AuthRequest',
  full_name='sae.AuthRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='sae.AuthRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='digest', full_name='sae.AuthRequest.digest', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_AUTHRESPONSE = descriptor.Descriptor(
  name='AuthResponse',
  full_name='sae.AuthResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SCRIPTREQUEST_KWARG = descriptor.Descriptor(
  name='KWArg',
  full_name='sae.ScriptRequest.KWArg',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='sae.ScriptRequest.KWArg.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='sae.ScriptRequest.KWArg.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_SCRIPTREQUEST = descriptor.Descriptor(
  name='ScriptRequest',
  full_name='sae.ScriptRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='access_profile', full_name='sae.ScriptRequest.access_profile', index=0,
      number=1, type=11, cpp_type=10, label=2,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script', full_name='sae.ScriptRequest.script', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kwargs', full_name='sae.ScriptRequest.kwargs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SCRIPTRESPONSE = descriptor.Descriptor(
  name='ScriptResponse',
  full_name='sae.ScriptResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='sae.ScriptResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FILECHECKSUM = descriptor.Descriptor(
  name='FileChecksum',
  full_name='sae.FileChecksum',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='sae.FileChecksum.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hash', full_name='sae.FileChecksum.hash', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_MANIFESTREQUEST = descriptor.Descriptor(
  name='ManifestRequest',
  full_name='sae.ManifestRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_MANIFESTRESPONSE = descriptor.Descriptor(
  name='ManifestResponse',
  full_name='sae.ManifestResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='files', full_name='sae.ManifestResponse.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SOFTWAREUPGRADEREQUEST = descriptor.Descriptor(
  name='SoftwareUpgradeRequest',
  full_name='sae.SoftwareUpgradeRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='names', full_name='sae.SoftwareUpgradeRequest.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FILECODE = descriptor.Descriptor(
  name='FileCode',
  full_name='sae.FileCode',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='sae.FileCode.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='code', full_name='sae.FileCode.code', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SOFTWAREUPGRADERESPONSE = descriptor.Descriptor(
  name='SoftwareUpgradeResponse',
  full_name='sae.SoftwareUpgradeResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='codes', full_name='sae.SoftwareUpgradeResponse.codes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_EVENTFILTERREQUEST = descriptor.Descriptor(
  name='EventFilterRequest',
  full_name='sae.EventFilterRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_EVENTFILTERRESPONSE = descriptor.Descriptor(
  name='EventFilterResponse',
  full_name='sae.EventFilterResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='expire', full_name='sae.EventFilterResponse.expire', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sources', full_name='sae.EventFilterResponse.sources', index=1,
      number=2, type=9, cpp_type=9, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_EVENTREQUEST_EVENTBODYITEM = descriptor.Descriptor(
  name='EventBodyItem',
  full_name='sae.EventRequest.EventBodyItem',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='sae.EventRequest.EventBodyItem.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='sae.EventRequest.EventBodyItem.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

_EVENTREQUEST = descriptor.Descriptor(
  name='EventRequest',
  full_name='sae.EventRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timestamp', full_name='sae.EventRequest.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip', full_name='sae.EventRequest.ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='sae.EventRequest.body', index=2,
      number=3, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_EVENTRESPONSE = descriptor.Descriptor(
  name='EventResponse',
  full_name='sae.EventResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PINGCHECKREQUEST = descriptor.Descriptor(
  name='PingCheckRequest',
  full_name='sae.PingCheckRequest',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='addresses', full_name='sae.PingCheckRequest.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PINGCHECKRESPONSE = descriptor.Descriptor(
  name='PingCheckResponse',
  full_name='sae.PingCheckResponse',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='unreachables', full_name='sae.PingCheckResponse.unreachables', index=0,
      number=1, type=9, cpp_type=9, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_MESSAGE.fields_by_name['request'].message_type = _REQUEST
_MESSAGE.fields_by_name['response'].message_type = _RESPONSE
_MESSAGE.fields_by_name['error'].message_type = _ERROR
_ERROR.fields_by_name['code'].enum_type = _ERRORCODE
_ACCESSPROFILE.fields_by_name['scheme'].enum_type = _ACCESSSCHEME
_SCRIPTREQUEST.fields_by_name['access_profile'].message_type = _ACCESSPROFILE
_SCRIPTREQUEST.fields_by_name['kwargs'].message_type = _SCRIPTREQUEST_KWARG
_MANIFESTRESPONSE.fields_by_name['files'].message_type = _FILECHECKSUM
_SOFTWAREUPGRADERESPONSE.fields_by_name['codes'].message_type = _FILECODE
_EVENTREQUEST.fields_by_name['body'].message_type = _EVENTREQUEST_EVENTBODYITEM

class Message(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGE

class Request(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

class Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

class Error(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ERROR

class AccessProfile(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCESSPROFILE

class PingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGREQUEST

class PingResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGRESPONSE

class RegisterRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERREQUEST

class RegisterResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERRESPONSE

class AuthRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHREQUEST

class AuthResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHRESPONSE

class ScriptRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class KWArg(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SCRIPTREQUEST_KWARG
  DESCRIPTOR = _SCRIPTREQUEST

class ScriptResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCRIPTRESPONSE

class FileChecksum(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILECHECKSUM

class ManifestRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANIFESTREQUEST

class ManifestResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANIFESTRESPONSE

class SoftwareUpgradeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOFTWAREUPGRADEREQUEST

class FileCode(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILECODE

class SoftwareUpgradeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOFTWAREUPGRADERESPONSE

class EventFilterRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTFILTERREQUEST

class EventFilterResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTFILTERRESPONSE

class EventRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class EventBodyItem(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _EVENTREQUEST_EVENTBODYITEM
  DESCRIPTOR = _EVENTREQUEST

class EventResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTRESPONSE

class PingCheckRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGCHECKREQUEST

class PingCheckResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGCHECKRESPONSE


_SAESERVICE = descriptor.ServiceDescriptor(
  name='SAEService',
  full_name='sae.SAEService',
  index=0,
  options=None,
  methods=[
  descriptor.MethodDescriptor(
    name='ping',
    full_name='sae.SAEService.ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='register',
    full_name='sae.SAEService.register',
    index=1,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='auth',
    full_name='sae.SAEService.auth',
    index=2,
    containing_service=None,
    input_type=_AUTHREQUEST,
    output_type=_AUTHRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='manifest',
    full_name='sae.SAEService.manifest',
    index=3,
    containing_service=None,
    input_type=_MANIFESTREQUEST,
    output_type=_MANIFESTRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='software_upgrade',
    full_name='sae.SAEService.software_upgrade',
    index=4,
    containing_service=None,
    input_type=_SOFTWAREUPGRADEREQUEST,
    output_type=_SOFTWAREUPGRADERESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='script',
    full_name='sae.SAEService.script',
    index=5,
    containing_service=None,
    input_type=_SCRIPTREQUEST,
    output_type=_SCRIPTRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='event_filter',
    full_name='sae.SAEService.event_filter',
    index=6,
    containing_service=None,
    input_type=_EVENTFILTERREQUEST,
    output_type=_EVENTFILTERRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='event',
    full_name='sae.SAEService.event',
    index=7,
    containing_service=None,
    input_type=_EVENTREQUEST,
    output_type=_EVENTRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ping_check',
    full_name='sae.SAEService.ping_check',
    index=8,
    containing_service=None,
    input_type=_PINGCHECKREQUEST,
    output_type=_PINGCHECKRESPONSE,
    options=None,
  ),
])

class SAEService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _SAESERVICE
class SAEService_Stub(SAEService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _SAESERVICE

