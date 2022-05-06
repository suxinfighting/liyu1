import pytest

sear_list = ['1', '2', 'aea']


@pytest.mark.parametrize('name', sear_list)
def test_search(name):
    assert name in sear_list
