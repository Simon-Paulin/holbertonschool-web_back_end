#!/usr/bin/env python3
"""
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    """
    st_index = (page - 1) * page_size
    end_index = page * page_size
    return (st_index, end_index)
