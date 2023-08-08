#!/usr/bin/env python3

""" This is a coroutine called async_generator that takes no arguments. """

import asyncio
import random


async def async_generator(max_delay: int = 10):
    """ Write a coroutine called async_generator that takes no arguments.
        The coroutine will loop 10 times, each time asynchronously wait 1
        second, then yield a random number between 0 and 10. Use the random
        module.
    """


for _ in range(10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(1)  # Wait 1 second asynchronously
    yield random.uniform(0, 10)
