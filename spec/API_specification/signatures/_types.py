"""
This file defines the types for type annotations.

The type variables should be replaced with the actual types for a given
library, e.g., for NumPy TypeVar('array') would be replaced with ndarray.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Literal, Optional, Sequence, Tuple, TypeVar, Union, Protocol
from enum import Enum

array = TypeVar('array')
device = TypeVar('device')
dtype = TypeVar('dtype')
SupportsDLPack = TypeVar('SupportsDLPack')
SupportsBufferProtocol = TypeVar('SupportsBufferProtocol')
PyCapsule = TypeVar('PyCapsule')
# ellipsis cannot actually be imported from anywhere, so include a dummy here
# to keep pyflakes happy. https://github.com/python/typeshed/issues/3556
ellipsis = TypeVar('ellipsis')

@dataclass
class finfo_object:
    """
    An object returned from :func:`~.finfo`. It has the following attributes:

    Attributes:
        bits (int): number of bits occupied by the floating-point data type.

        eps (float): difference between 1.0 and the next smallest representable floating-point number larger than 1.0 according to the IEEE-754 standard.

        max (float): largest representable number.

        min (float): smallest representable number.

        smallest_normal (float): smallest positive floating-point number with full precision.
"""
    bits: int
    eps: float
    max: float
    min: float
    smallest_normal: float

@dataclass
class iinfo_object:
    bits: int
    max: int
    min: int


_T_co = TypeVar("_T_co", covariant=True)

class NestedSequence(Protocol[_T_co]):
    def __getitem__(self, key: int, /) -> Union[_T_co, NestedSequence[_T_co]]: ...
    def __len__(self, /) -> int: ...


__all__ = ['Any', 'List', 'Literal', 'NestedSequence', 'Optional',
'PyCapsule', 'SupportsBufferProtocol', 'SupportsDLPack', 'Tuple', 'Union',
'array', 'device', 'dtype', 'ellipsis', 'finfo_object', 'iinfo_object', 'Enum']
