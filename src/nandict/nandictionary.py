from collections.abc import Iterable, Mapping, MutableMapping
from math import nan
from typing import Any, overload

from nancipher import as_int


class NaNDict(dict):
    """A Python Dictionary that can only accept a single NaN as a key"""

    _mappings = {as_int(nan): nan}

    @overload
    def __init__(self, init: MutableMapping): ...
    @overload
    def __init__(self, **kwargs): ...

    def __init__(self, init: MutableMapping | None = None, **kwargs):
        super().__init__()
        self.update(init, **kwargs)

    def _get_key_mapping(self, key: float) -> float:
        """Get the mapping for a specific NaNKey"""
        if key == key:
            return key
        key_as_int = as_int(key)
        if key_as_int not in self._mappings:
            self._mappings[key_as_int] = key
        return self._mappings[key_as_int]

    def __setitem__(self, key, value):
        key = self._get_key_mapping(key)
        super().__setitem__(key, value)

    def __getitem__(self, key):
        key = self._get_key_mapping(key)
        return super().__getitem__(key)

    def get(self, __key, default=None, /):
        __key = self._get_key_mapping(__key)
        try:
            return self[__key]
        except KeyError:
            return default

    def setdefault(self, key, default=None, /):
        key = self._get_key_mapping(key)
        super().setdefault(key, default)

    def pop(self, key, *args):
        key = self._get_key_mapping(key)
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
        key = self._get_key_mapping(key)
        return super().__contains__(key)
