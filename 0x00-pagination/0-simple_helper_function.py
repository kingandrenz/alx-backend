#!/usr/bin/env python3
"""this is a pagination module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a start index and an end index as tuple
    """

    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
