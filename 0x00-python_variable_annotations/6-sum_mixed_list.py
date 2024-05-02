#!/usr/bin/env python3
""" returns the floor of the float. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the floor of the float. """
    sum_total = 0
    for num in mxd_lst:
        sum_total += num
    return sum_total
