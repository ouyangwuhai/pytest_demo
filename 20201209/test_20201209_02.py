import pytest

def test_a():
    assert 1 == 1


def test_b():
    assert 2==3

#pytest test_20201209_02.py::test_b

@pytest.mark.aaa
def test_b():
    assert 2==2

#pytest -m aaa 执行标志