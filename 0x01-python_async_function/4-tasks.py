#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
 seconds and eventually returns it."""

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ rondom wait"""
    delay_list = []
    for _ in range(n):
        result = await task_wait_random(max_delay)
        delay_list.append(result)
    return sorted(delay_list)
