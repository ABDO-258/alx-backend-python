#!/usr/bin/env python3
""" returns a list tuble.. """
from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns a list tuble.. """
    if lst:
        return lst[0]
    else:
        return None
