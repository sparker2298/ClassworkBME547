import pytest


def test_get_line():
    from make_line import get_line
    tup1 = (2, 2)
    tup2 = (3, 3)
    new_x = 1
    answer = get_line(tup1, tup2, new_x)
    assert answer == 1
