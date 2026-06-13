from collections.abc import Iterable, Mapping, MutableMapping
from math import isnan, nan
from typing import Any, overload


class NaNDict(dict):
    """A Python Dictionary that can only accept a single NaN as a key"""

    @overload
    def __init__(self, init: MutableMapping): ...
    @overload
    def __init__(self, **kwargs): ...

    def __init__(self, init: MutableMapping | None = None, **kwargs):
        super().__init__()
        self.update(init, **kwargs)

    def __setitem__(self, key, value):
        if key != key and isnan(key):
            key = nan
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key != key and isnan(key):
            key = nan
        return super().__getitem__(key)

    def get(self, __key, default=None, /):
        if __key != __key and isnan(__key):
            __key = nan
        try:
            return self[__key]
        except KeyError:
            return default

    def setdefault(self, key, default=None, /):
        if key != key and isnan(key):
            key = nan
        super().setdefault(key, default)

    def pop(self, key, *args):
        if key != key and isnan(key):
            key = nan
        return super().pop(key, *args)

    def update(self, mapping: MutableMapping | Iterable | None, **kwargs):  # type: ignore
        match mapping:
            case Mapping():
                for k, v in mapping.items():
                    self[k] = v
            case None:
                pass
            case _:
                for k, v in mapping:
                    self[k] = v
        if kwargs:
            self.update(kwargs)

    def __contains__(self, key: Any):
        if key != key and isnan(key):
            key = nan
        return super().__contains__(key)
