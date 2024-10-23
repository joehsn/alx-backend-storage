#!/usr/bin/env python3

"""
    0. Writing strings to Redis tasks's module.
"""

import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
            Retrieves a value from a Redis.
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
            Coarce the retrieved value into a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
            Coarce the retrieved value into a intger.
        """
        return self.get(key, lambda x: int(x))

