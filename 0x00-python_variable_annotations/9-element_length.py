#!/usr/bin/env python3
""" returns a list tuble.. """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list tuble.. """
    return [(i, len(i)) for i in lst]
