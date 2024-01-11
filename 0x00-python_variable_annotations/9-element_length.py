#!/usr/bin/env python3
"""This module for a type annotated element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a sequence a return a list"""
    return [(i, len(i)) for i in lst]
