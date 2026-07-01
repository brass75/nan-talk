from collections.abc import Callable

from .nancipher import NaNCipher

nan_with_payload: Callable = NaNCipher.nan_with_payload
payload_from_nan: Callable = NaNCipher.payload_from_nan
as_int: Callable = NaNCipher.as_int

__all__ = [
    'NaNCipher',
    'payload_from_nan',
    'nan_with_payload',
    'as_int',
]
