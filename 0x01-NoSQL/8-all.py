#!/usr/bin/env python3

"""
    8. List all documents in Python task's module.
"""


def list_all(mongo_collection):
    """
        A function that lists all documents in a collection.
    """
    return [doc for doc in mongo_collection.find()]