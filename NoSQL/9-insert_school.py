#!/usr/bin/env python3
"""Insert a document in Python l"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python l"""
    result = mongo_collection.insert_one(kwargs)
    insert_id = result.inserted_id
    return insert_id
