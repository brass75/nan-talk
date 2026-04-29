from nandict import NaNCounter


def test_nancounter():
    d = {float('nan') for _ in range(10)}
    assert len(d) == 10
    d.update(range(10))
    assert len(d) == 20
    nc = NaNCounter(d)
    assert len(nc) == 11
    assert nc[float('nan')] == 10
