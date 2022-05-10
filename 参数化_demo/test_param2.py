import pytest


@pytest.mark.parametrize("test_input, test_expect", [("3+5", 8), ("2+5", 7), ("7+5", 12)],
                         ids=["number1", "number2", "number3"])
def test_mark_more(test_input, test_expect):
    assert eval(test_input) == test_expect
