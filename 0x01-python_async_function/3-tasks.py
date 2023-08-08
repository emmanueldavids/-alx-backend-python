#!/usr/bin/env python3

import asyncio
import random
from typing import Any


async def wait_random(max_delay=10):
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    loop = asyncio.get_event_loop()
    coro = wait_random(max_delay)
    task = loop.create_task(coro)
    return task
