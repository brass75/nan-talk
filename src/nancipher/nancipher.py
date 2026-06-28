import struct
from collections.abc import Iterator
from typing import Any

MIN_NAN: int = 0x7FC0_0000


class NaNCipher:
    def __init__(self, text: str):
        """
        Constructor for NaNCipher

        :param text: The text to encode
        """
        self._encoded = list(map(self.nan_with_payload, text))

    @classmethod
    def nan_with_payload(cls, payload: str) -> float:
        """
        Create a NaN object with a payload

        :param payload: The string payload to encode in the NaN object
        :return: A NaN object with a payload encoded in it
        """
        return struct.unpack('f', struct.pack('i', MIN_NAN | ord(payload)))[0]

    @classmethod
    def payload_from_nan(cls, nan_payload: float) -> str:
        """
        Extract the payload from a NaN object

        :param nan_payload: The NaN object with the payload
        :return: The payload from the NaN object
        """
        return chr(cls._as_int(nan_payload) & ~MIN_NAN)

    @classmethod
    def _as_int(cls, nan_value: float) -> int:
        """
        Convert a NaN into an int for comparison

        :param nan_value: The NaN to convert
        :return: The NaN bytes as an int
        """
        return struct.unpack('i', struct.pack('f', nan_value))[0]

    def __iter__(self) -> Iterator[float]:
        """Iterator of encoded NaN objects"""
        yield from self._encoded

    def __repr__(self) -> str:
        """Repr for NaNCiper"""
        return repr(self._encoded)

    def __str__(self) -> str:
        """String representation of the decoded objects"""
        return ''.join(map(self.payload_from_nan, self))

    def __len__(self) -> int:
        """Length of the encoded string"""
        return len(self._encoded)

    def __eq__(self, other: str | type['NaNCipher'] | Any) -> bool:
        """Equality check"""
        cls = type(self)
        match other:
            case str():
                if len(other) != len(self):
                    return False
                return other == str(self)
            case cls():
                if len(other) != len(self):  # type: ignore
                    return False
                return all(self._as_int(o) == other._as_int(s) for o, s in zip(self, other))  # type: ignore
            case _:
                return False
