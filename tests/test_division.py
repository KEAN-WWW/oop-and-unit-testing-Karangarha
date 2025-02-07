"""Test Division"""
import pytest
from app.Division import divide

def test_division():
    """Testing different numbers"""
    assert divide(4,2) == 2
    assert divide(1024, 256) == 4

def test_divide_zero_exception():
    """case of error"""
    with pytest.raises(ZeroDivisionError):
        divide(1,0)
