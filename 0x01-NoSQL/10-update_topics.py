#!/usr/bin/env python3
"""
    10. Change school topics task's module.
"""


def update_topics(mongo_collection, name, topics):
    """
        A function that changes all topics of
        a school document based on the name.
    """
    mongo_collection.update_many(
        { 'name': name },
        { '$set': { 'topics': topics } }
    )
