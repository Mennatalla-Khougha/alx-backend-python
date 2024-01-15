#!/usr/bin/env python3
"""This module define the wait_n function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    The `wait_n` function takes in two parameters, `n` and `max_delay`,\
        and returns a sorted list of `n`
    random delay times.

    :param n: The number of tasks to wait for
    :type n: int
    :param max_delay: The `max_delay` parameter represents the maximum amount\
        of time (in seconds) that
    each task should wait before completing
    :type max_delay: int
    :return: The function `wait_n` returns a sorted list of floats.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*tasks)
    return sorted(result)
