# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: task.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 29, 0, "", "task.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ntask.proto\x12\x0e\x65vent_pipeline"V\n\x0bTaskRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\n\n\x02\x66n\x18\x02 \x01(\x0c\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x04 \x01(\x0c\x12\x0e\n\x06kwargs\x18\x05 \x01(\x0c">\n\x0cTaskResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06result\x18\x02 \x01(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\t"\x9f\x01\n\nTaskStatus\x12\x31\n\x06status\x18\x01 \x01(\x0e\x32!.event_pipeline.TaskStatus.Status\x12\x0e\n\x06result\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t"=\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xa4\x01\n\x0cTaskExecutor\x12\x46\n\x07\x45xecute\x12\x1b.event_pipeline.TaskRequest\x1a\x1c.event_pipeline.TaskResponse"\x00\x12L\n\rExecuteStream\x12\x1b.event_pipeline.TaskRequest\x1a\x1a.event_pipeline.TaskStatus"\x00\x30\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "task_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_TASKREQUEST"]._serialized_start = 30
    _globals["_TASKREQUEST"]._serialized_end = 116
    _globals["_TASKRESPONSE"]._serialized_start = 118
    _globals["_TASKRESPONSE"]._serialized_end = 180
    _globals["_TASKSTATUS"]._serialized_start = 183
    _globals["_TASKSTATUS"]._serialized_end = 342
    _globals["_TASKSTATUS_STATUS"]._serialized_start = 281
    _globals["_TASKSTATUS_STATUS"]._serialized_end = 342
    _globals["_TASKEXECUTOR"]._serialized_start = 345
    _globals["_TASKEXECUTOR"]._serialized_end = 509
# @@protoc_insertion_point(module_scope)
