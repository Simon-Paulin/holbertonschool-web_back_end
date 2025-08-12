#!/usr/bin/env python3
"""schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic"""
    same_schools = mongo_collection.find({"topics": topic})
    return list(same_schools)
