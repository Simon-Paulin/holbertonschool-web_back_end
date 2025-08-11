#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function """
    st_index = (page - 1) * page_size
    end_index = page + page_size
    return (st_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        st_index, end_index = index_range(page, page_size)
        data = self.dataset()
        
        
        if st_index >= len(data):
            return []
        return data[st_index:end_index]
def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_page = self.get_page(page, page_size)
        total_rows = len(self.dataset())

        if total_rows > 0:
            total_pages = math.ceil(total_rows / page_size)
        else:
            total_pages = 0

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
