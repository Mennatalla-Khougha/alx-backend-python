#!/usr/bin/env python3
"""This module define the async_comprehension function"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The function `async_comprehension` uses an async generator to generate
    values and returns a list of those values.
    :return: a list of values obtained from an async generator.
    """
    result = [value async for value in async_generator()]
    return result
