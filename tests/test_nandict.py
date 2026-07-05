from math import nan

import pytest

from nandict import NaNDict


@pytest.mark.parametrize(
    'init, kwargs, expected',
    [
        ({float('nan'): n for n in range(10)}, {}, {nan: 9}),
        (([(float('nan'), 1), (2, 3)]), {}, {nan: 1, 2: 3}),
        (None, {'4': 5}, {'4': 5}),
        ({float('inf'): 1, float('inf'): 2, **{float('nan'): n for n in range(10)}}, None, {float('inf'): 2, nan: 9}),
    ],
)
def test_single_nan(init, kwargs, expected):
    assert init or kwargs and not init and kwargs
    if init:
        assert NaNDict(init) == expected
    else:
        assert NaNDict(**kwargs) == expected


def test_setting_and_getting():
    d = NaNDict({float('nan'): 2})
    assert d[float('nan')] == 2
    d[float('nan')] = 3
    assert d[float('nan')] == 3
    assert d == {nan: 3}
    assert d != {float('nan'): 3}
    assert float('nan') in d


def test_get():
    d = NaNDict({1: 2})
    assert d.get(float('nan')) is None
    d[float('nan')] = 3
    assert d.get(float('nan')) == 3
    assert d.get(5, 'Nope') == 'Nope'


def test_setdefault():
    d = NaNDict()
    d.setdefault(float('nan'))
    assert d == {nan: None}


def test_pop():
    d = NaNDict({float('nan'): 2})
    assert d.pop(float('nan')) == 2


def test_invalid_key_type():
    d = NaNDict()
    with pytest.raises(ValueError):
        d[[1, 2, 3]] = 4
