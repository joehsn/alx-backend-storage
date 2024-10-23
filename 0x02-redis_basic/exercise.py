#!/usr/bin/env python3

"""
0. Writing strings to Redis tasks's module.
1. Reading from Redis and recovering original type task's module.
2. Incrementing values task's module.
"""

import uuid
import redis
from typing import Union, Callable
import functools

def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of inputs and outputs for a particular function.
            Stores the inputs and outputs in Redis lists.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.
            The count is stored in Redis using the method's qualified name as the key.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

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

    @count_calls
    @call_history
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

