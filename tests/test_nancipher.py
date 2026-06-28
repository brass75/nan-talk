from math import isnan

import pytest
from conftest import TEST_STRING

from nancipher import NaNCipher


def test_nancipher():
    """Test NaNCipher"""
    encoded = NaNCipher(TEST_STRING)
    assert TEST_STRING == encoded
    assert all(isnan(o) for o in encoded)


@pytest.mark.parametrize(
    'value, response',
    [
        (NaNCipher(TEST_STRING), True),
        (TEST_STRING, True),
        (123, False),
        ('123', False),
        (NaNCipher('123'), False),
    ],
)
def test_equality(value, response):
    """Test equality comparisons"""
    assert (NaNCipher(TEST_STRING) == value) == response


def test_repr():
    """Test the repr"""
    assert repr(NaNCipher(TEST_STRING)) == f'[{", ".join("nan" for _ in range(len(TEST_STRING)))}]'
