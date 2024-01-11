#!/usr/bin/env python3
"""This module for a type annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and return a float"""
    def multiply(n: float) -> float:
        """Takes a float and return a float"""
        return n * multiplier
    return multiply
