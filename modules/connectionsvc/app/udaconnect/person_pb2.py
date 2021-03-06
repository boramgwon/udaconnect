# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cperson.proto\"X\n\x06Person\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x07\n\x05\x45mpty\"\x1d\n\x08PersonId\x12\x11\n\tperson_id\x18\x01 \x01(\x05\"&\n\nPersonList\x12\x18\n\x07persons\x18\x01 \x03(\x0b\x32\x07.Person2u\n\rPersonService\x12\x1c\n\x06\x43reate\x12\x07.Person\x1a\x07.Person\"\x00\x12 \n\x08Retrieve\x12\t.PersonId\x1a\x07.Person\"\x00\x12$\n\x0bRetrieveAll\x12\x06.Empty\x1a\x0b.PersonList\"\x00\x62\x06proto3'
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Person.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Person.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Person.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='Person.company_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=104,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=113,
)


_PERSONID = _descriptor.Descriptor(
  name='PersonId',
  full_name='PersonId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='PersonId.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=144,
)


_PERSONLIST = _descriptor.Descriptor(
  name='PersonList',
  full_name='PersonList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persons', full_name='PersonList.persons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=184,
)

_PERSONLIST.fields_by_name['persons'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['PersonId'] = _PERSONID
DESCRIPTOR.message_types_by_name['PersonList'] = _PERSONLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  })
_sym_db.RegisterMessage(Person)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

PersonId = _reflection.GeneratedProtocolMessageType('PersonId', (_message.Message,), {
  'DESCRIPTOR' : _PERSONID,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonId)
  })
_sym_db.RegisterMessage(PersonId)

PersonList = _reflection.GeneratedProtocolMessageType('PersonList', (_message.Message,), {
  'DESCRIPTOR' : _PERSONLIST,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonList)
  })
_sym_db.RegisterMessage(PersonList)



_PERSONSERVICE = _descriptor.ServiceDescriptor(
  name='PersonService',
  full_name='PersonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=186,
  serialized_end=303,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='PersonService.Create',
    index=0,
    containing_service=None,
    input_type=_PERSON,
    output_type=_PERSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='PersonService.Retrieve',
    index=1,
    containing_service=None,
    input_type=_PERSONID,
    output_type=_PERSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveAll',
    full_name='PersonService.RetrieveAll',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PERSONLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONSERVICE)

DESCRIPTOR.services_by_name['PersonService'] = _PERSONSERVICE

# @@protoc_insertion_point(module_scope)
