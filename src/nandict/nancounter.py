from collections.abc import Iterable

from .nandictionary import NaNDict


class NaNCounter(NaNDict):
    def __init__(self, iterable: Iterable):
        for val in iterable:
            self[val] = self.setdefault(val, 0) + 1

    def __missing__(self, key) -> int:
        """Handle missing key"""
        # Since this is supposed to be essentially equivalent to collections.Counter it should
        # return 0 on a missing key
        return 0
