"""Test Addition"""
from app.addition import add

def test_addition():
    """Testing different numbers"""
    assert add(3,8) == 11
    assert add(8, 92)==100
