from helloarefin.operations import add, subtract

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtraction():
    assert subtract(5, 2) == 3
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
