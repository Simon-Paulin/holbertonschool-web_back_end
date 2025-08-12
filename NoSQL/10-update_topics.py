#!/usr/bin/env python3
""" changes topic"""


def update_topics(mongo_collection, name, topics):
    """ changes topic"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
