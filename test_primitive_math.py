
import primitive_math
import pytest

@pytest.mark.parametrize("test_x, test_y ,expected", [(3, 4, 7), (2, 7, 9), (2,8,10), (56, 17, 73)])

def test_add(test_x, test_y, expected):
    assert(primitive_math.add(test_x, test_y) == expected)
    
@pytest.mark.parametrize("test_x, test_y ,expected", [(3, 4, 12), (2, 7, 14), (2,8,16), (56, 17, 952)])

def test_multiply(test_x, test_y, expected):
    assert(primitive_math.multiply(test_x, test_y) == expected)