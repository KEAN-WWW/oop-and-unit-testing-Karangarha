from app.subtraction import subtract

def test_subtraction():
    assert subtract(6, 8) == -2
    assert subtract(10, 8) == 2
