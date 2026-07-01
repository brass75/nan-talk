from collections import Counter

from conftest import TEST_STRING

from nandict import NaNCipher, NaNCounter, nan_with_payload


def test_nancounter():
    d = {float('nan') for _ in range(10)}
    assert len(d) == 10
    d.update(range(10))
    assert len(d) == 20
    nc = NaNCounter(d)
    assert len(nc) == 11
    assert nc[float('nan')] == 10


def test_nancounter_multiple_nans():
    """Test that NaNCounter works properly with differently valued NaNs"""
    counter = NaNCounter(NaNCipher(TEST_STRING))
    text_counter = Counter(TEST_STRING)
    for c in TEST_STRING:
        encoded = nan_with_payload(c)
        assert counter.get(encoded) == text_counter[c]
