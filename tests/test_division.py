import pytest
from app.Division import divide

def test_division():
    assert divide(4,2) == 2
    assert divide(1024, 256) == 4

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)