#!/usr/bin/env python3
"""This module for a type annotated safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Takes a an element af Any type a return a it's first element"""
    if lst:
        return lst[0]
    else:
        return None
