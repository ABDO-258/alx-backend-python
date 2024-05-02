#!/usr/bin/env python3
""" returns a tuble.. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuble. """
    return k, v ** 2
