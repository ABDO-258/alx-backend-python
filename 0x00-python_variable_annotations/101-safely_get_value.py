#!/usr/bin/env python3
""" docc string for scribt. """
from typing import Mapping, Union, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ docc string for methode. """
    if key in dct:
        return dct[key]
    else:
        return default
