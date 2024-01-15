#!/usr/bin/env python3
"""This module define the task_wait_n async function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The function `task_wait_n` takes in two parameters, `n` and `max_delay`,\
        and creates `n` tasks that wait for a random amount of time up to\
        `max_delay`, and then returns a list of the times it took for each\
        task to complete.

    :param n: The parameter `n` represents the number of tasks to be executed\
        concurrently
    :type n: int
    :param max_delay: The `max_delay` parameter represents the maximum amount\
        of time (in seconds) that
    each task can wait before completing
    :type max_delay: int
    :return: a list of floats.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    result = [await t for t in asyncio.as_completed(tasks)]
    return result
