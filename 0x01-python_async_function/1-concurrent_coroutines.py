#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
 seconds and eventually returns it."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ rondom wait"""
    delay_list = []
    for _ in range(n):
        result = await asyncio.create_task(wait_random(max_delay))
        delay_list.append(result)
    return sorted(delay_list)
