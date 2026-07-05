from collections.abc import Hashable, Iterable, Mapping, MutableMapping
from math import nan
from typing import Any, overload

from .nancipher import as_int


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

    def _get_key_mapping(self, key: Any) -> Hashable:
        """
        Get the mapping for a specific NaNKey

        :param key: The key to get the mapping for
        :return: The key to use
        :raises: ValueError if the key is not Hashable.
        """
        match key:
            case float():
                return self._mappings.setdefault(as_int(key), key) if key != key else key
            case _:
                if not isinstance(key, Hashable):
                    raise ValueError(f'Provided key is not Hashable. {repr(key)}')
                return key

    def __setitem__(self, key: Hashable, value: Any) -> None:
        super().__setitem__(self._get_key_mapping(key), value)

    def __getitem__(self, key: Hashable):
        return super().__getitem__(self._get_key_mapping(key))

    def get(self, __key: Hashable, default: Any = None, /):
        try:
            return self[self._get_key_mapping(__key)]
        except KeyError:
            return default

    def setdefault(self, key: Hashable, default: Any = None, /):
        super().setdefault(self._get_key_mapping(key), default)

    def pop(self, key: Hashable, *args):
        return super().pop(self._get_key_mapping(key), *args)

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

    def __contains__(self, key: Hashable):
        return super().__contains__(self._get_key_mapping(key))
