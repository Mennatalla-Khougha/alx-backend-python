#!/usr/bin/env python3
"""This module is defining the measure_runtime function"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The `measure_runtime` function measures the runtime of an asynchronous
    comprehension.
    :return: The function `measure_runtime` returns the total runtime in
    seconds as a float.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return end - start
