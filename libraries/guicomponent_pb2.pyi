from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    STATUS_SUCCESS: _ClassVar[Status]
    STATUS_COMPONENT_NOT_FOUND: _ClassVar[Status]
    STATUS_COMMAND_NOT_AVAILABLE: _ClassVar[Status]
    STATUS_COMPONENT_DISABLED: _ClassVar[Status]
    STATUS_COMPONENT_NOT_FOCUSED: _ClassVar[Status]
    STATUS_WRONG_SIZE: _ClassVar[Status]
STATUS_UNSPECIFIED: Status
STATUS_SUCCESS: Status
STATUS_COMPONENT_NOT_FOUND: Status
STATUS_COMMAND_NOT_AVAILABLE: Status
STATUS_COMPONENT_DISABLED: Status
STATUS_COMPONENT_NOT_FOCUSED: Status
STATUS_WRONG_SIZE: Status

class Component(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ComponentEditor(_message.Message):
    __slots__ = ("component", "text")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    component: Component
    text: str
    def __init__(self, component: _Optional[_Union[Component, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class GuiResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    message: str
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ScreenshotRequest(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class ScreenshotResponse(_message.Message):
    __slots__ = ("status", "image", "imageFormat", "description")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGEFORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    image: bytes
    imageFormat: str
    description: str
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., image: _Optional[bytes] = ..., imageFormat: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
