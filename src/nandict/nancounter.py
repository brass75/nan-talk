from collections.abc import Iterable

from .nandictionary import NaNDict


class NaNCounter(NaNDict):
    def __init__(self, iterable: Iterable):
        for val in iterable:
            self.setdefault(val, 0)
            self[val] += 1
