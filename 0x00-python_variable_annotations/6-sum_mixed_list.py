#!/usr/bin/env python3
"""This module for a type annotated sum_mixed_list function"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Takes a list of float and int and return their float sum"""
    sum: float = 0.0
    for i in mxd_list:
        sum += i
    return sum
