import pytest


@pytest.mark.case1
def test_case1():
    assert 1 == 1


@pytest.mark.case2
def test_case2():
    assert 2 == 2


@pytest.mark.case3
def test_case3():
    assert 3 == 3

