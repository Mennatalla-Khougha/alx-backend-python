#!/usr/bin/env python3
"""This module for a type annotated sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a float list and return their float sum"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
