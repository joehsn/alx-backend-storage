#!/usr/bin/env python3
"""
    11. Where can I learn Python? task's module.
"""


def schools_by_topic(mongo_collection, topic):
    """
        A function that returns the list of school
        having a specific topic.
    """
    return [doc for doc in mongo_collection.find({
        'topics': {
            '$elemMatch': {
                '$eq': topic
            }
        }
    })]
