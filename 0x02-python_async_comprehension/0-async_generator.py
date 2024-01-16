#!/usr/bin/env python3
"""This Module define the async_generator function"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    The above function is an asynchronous generator that yields random
    floating-point numbers between 1 and 10 with a delay of 1 second between
    each yield.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
