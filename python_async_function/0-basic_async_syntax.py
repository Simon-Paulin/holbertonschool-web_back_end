#!/usr/bin/env python3
"""
async chrono
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    random delay
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
