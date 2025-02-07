"""Test multiplication"""
from app.multiplication import multiply

def test_multiplication():
    """Testing different numbers"""
    assert multiply(9, 5) == 45
    assert multiply(6,0) == 0
