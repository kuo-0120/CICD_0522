from src.calculate import add, sub, mut


def test_add_func():
    assert add(1, 2) == 3


def test_sub_func():
    assert sub(5, 2) == 3


def test_mut_func():
    assert mut(2, 3) == 6
