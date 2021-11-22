
import primitive_math
import pytest

@pytest.mark.parametrize("test_x, test_y ,expected", [(3, 4, 7), (2, 7, 9), (2,8,10), (56, 17, 73)])

def test_add(test_x, test_y, expected):
    assert(primitive_math.add(test_x, test_y) == expected)
    