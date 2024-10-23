#!/usr/bin/env python3

"""
    0. Writing strings to Redis tasks's module.
"""

import uuid
import redis
from typing import Union


class Cache:
    """
        Redis cache store.
    """
    def __init__(self) -> None:
        """
            Initializes a Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Stores a key-value pair and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
