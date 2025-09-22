import math_uitls

def test_add():
    assert math_uitls.add(2, 3) == 5
    assert math_uitls.add(-1, 1) == 0
    assert math_uitls.add(0, 0) == 0
    assert math_uitls.add(-1, -1) == -2