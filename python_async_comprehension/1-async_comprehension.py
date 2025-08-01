#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """task and then write a coroutine called async_comprehension"""
    return [value async for value in async_generator()]
