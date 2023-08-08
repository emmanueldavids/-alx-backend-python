#!/usr/bin/env python3
""" Take the code from wait_n and alter it into a new function
    task_wait_n. The code is nearly identical to wait_n except
    task_wait_random is being called.
"""


import asyncio
from typing import List
wait_n = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ created a new asynchronous function task_wait_random
        that returns the result of the wait_random coroutine
        after awaiting the task.
    """

    tasks = [wait_n(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
