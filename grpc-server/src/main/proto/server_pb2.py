# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x05proto\x1a\x1egoogle/protobuf/wrappers.proto\"+\n\x15\x43orrectGrammarRequest\x12\x12\n\ntranscript\x18\x01 \x01(\t\"p\n\x16\x43orrectGrammarResponse\x12\x19\n\x11\x63orrectTranscript\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12-\n\x07message\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue2\\\n\tNlpServer\x12O\n\x0e\x43orrectGrammar\x12\x1c.proto.CorrectGrammarRequest\x1a\x1d.proto.CorrectGrammarResponse\"\x00\x42\x08Z\x06/protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006/proto'
  _CORRECTGRAMMARREQUEST._serialized_start=55
  _CORRECTGRAMMARREQUEST._serialized_end=98
  _CORRECTGRAMMARRESPONSE._serialized_start=100
  _CORRECTGRAMMARRESPONSE._serialized_end=212
  _NLPSERVER._serialized_start=214
  _NLPSERVER._serialized_end=306
# @@protoc_insertion_point(module_scope)
