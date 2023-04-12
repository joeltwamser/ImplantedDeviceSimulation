from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Frequency(_message.Message):
    __slots__ = ["cycles_per_second"]
    CYCLES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    cycles_per_second: float
    def __init__(self, cycles_per_second: _Optional[float] = ...) -> None: ...

class GraphSamples(_message.Message):
    __slots__ = ["samples"]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    samples: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, samples: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class Initialize(_message.Message):
    __slots__ = ["init_message"]
    INIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    init_message: str
    def __init__(self, init_message: _Optional[str] = ...) -> None: ...

class Phase(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: float
    def __init__(self, number: _Optional[float] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
