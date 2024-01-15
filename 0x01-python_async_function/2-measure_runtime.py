#!/usr/bin/env python3
"""This module if for defining the measure_time function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    The `measure_time` function measures the average time it takes to\
        execute the `wait_n` function `n` times with a maximum delay of\
        `max_delay`.

    :param n: The parameter `n` represents the number of tasks or operations\
        that need to be executed
    :type n: int
    :param max_delay: The `max_delay` parameter represents the maximum delay\
        in seconds that each
    individual task can have
    :type max_delay: int
    :return: the average time taken for each task to complete.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
