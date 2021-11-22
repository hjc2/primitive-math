
import pytest
import primitive_math

@pytest.mark.parametrize("test_x, expected", [(3, 4), (5, 6), (12, 13), (56, 57)])
def test_increment(test_x, expected):
    assert(primitive_math.increment(test_x) == expected)


@pytest.mark.parametrize("test_x, expected", [(4, 3), (6, 5), (13, 12), (57, 56)])
def test_decrement(test_x, expected):
    assert(primitive_math.decrement(test_x) == expected)


@pytest.mark.parametrize("test_x, test_y ,expected", [(3, 4, 7), (2, 7, 9), (2, 8, 10), (56, 17, 73)])
def test_add(test_x, test_y, expected):
    assert(primitive_math.add(test_x, test_y) == expected)


@pytest.mark.parametrize("test_x, test_y ,expected", [(3, 4, 12), (2, 7, 14), (2, 8, 16), (56, 17, 952)])
def test_multiply(test_x, test_y, expected):
    assert(primitive_math.multiply(test_x, test_y) == expected)


@pytest.mark.parametrize("test_x, test_y ,expected", [(4, 3, 64), (2, 3, 8), (7, 2, 49), (5, 3, 125)])
def test_power(test_x, test_y, expected):
    assert(primitive_math.power(test_x, test_y) == expected)
