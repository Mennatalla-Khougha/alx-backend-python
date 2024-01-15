#!/usr/bin/env python3
"""Tis module define the wait_random async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    The `wait_random` function asynchronously waits for a random\
        amount of time between 0 and
    `max_delay` and then returns the delay.

    :param max_delay: The max_delay parameter is an optional integer \
        that specifies the maximum delay in
    seconds that the function should wait before returning a value.\
        If no value is provided for
    max_delay, it defaults to 10, defaults to 10
    :type max_delay: int (optional)
    :return: The function `wait_random` returns a float value,\
        which is the randomly generated delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
