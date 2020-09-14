import math_func
import pytest

@pytest.mark.parametrize('x, y, result', [
    (7, 3, 10),
    ('Hello ', 'World', 'Hello World'),
    (10.5, 25.5, 36)
])
def test_add(x, y, result):
    assert math_func.add(x, y) == result
    

    