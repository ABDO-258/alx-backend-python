#!/usr/bin/env python3
""" returns a tuble.. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a result of multipication. """
    def result(num: float) -> float:
        """returns a result of multipication"""
        return num * multiplier
    return result
