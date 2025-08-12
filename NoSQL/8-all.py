#!/usr/bin/env python3
"""list all documents"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.school


def list_all(mongo_collection):
    """list"""
    docs = list (mongo_collection.find())
    if len(docs) == 0:
        return[]
    return docs
