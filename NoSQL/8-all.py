#!/usr/bin/env python3
"""list all documents"""


def list_all(mongo_collection):
    """"""
    docs = list (mongo_collection.find())
    if len(docs) == 0:
        return[]
    return docs
