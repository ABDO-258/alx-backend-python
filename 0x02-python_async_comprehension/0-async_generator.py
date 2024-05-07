#!/usr/bin/env python3
"""  loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[Any,Any]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
