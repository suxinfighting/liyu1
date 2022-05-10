import pytest

@pytest.mark.parametrize("wd", ["wq","wqe", "qwe"])
@pytest.mark.parametrize("code", ["1","2", "3"])
def test_dkej(wd, code):
    print(f"wd:{wd}, code:{code}")