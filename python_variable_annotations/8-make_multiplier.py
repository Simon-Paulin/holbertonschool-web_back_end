#!/usr/bin/env python3
"""
mulplier with a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier with a float
    """
    def multip(x: float) -> float:
        """
        mult func
        """
        return x * multip
    return multip
