# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trec.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x02 \x01(\t24\n\x07Service\x12)\n\x08SayHello\x12\r.HelloRequest\x1a\x0e.HelloResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rec_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=13
  _globals['_HELLOREQUEST']._serialized_end=41
  _globals['_HELLORESPONSE']._serialized_start=43
  _globals['_HELLORESPONSE']._serialized_end=75
  _globals['_SERVICE']._serialized_start=77
  _globals['_SERVICE']._serialized_end=129
# @@protoc_insertion_point(module_scope)