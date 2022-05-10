import pytest


@pytest.mark.skip
def test_aaa():
    assert True


@pytest.mark.skip(reason="代码没有实现")
def test_bbb():
    assert True
