#!/usr/bin/env python3
"""This module for a type annotated to_kv function"""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a str and an int or float and return a tuple"""
    sq: Union[int, float] = math.pow(v, 2)
    return (k, sq)
