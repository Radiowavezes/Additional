import pytest
from fraction import Fraction


@pytest.mark.parametrize("x1,x2,y1,y2,r1,r2", [
    (1, 2, 1, 4, 3, 4),
    (2, 3, 5, 4, 13, 12)
    ])
def test_add_fraction(x1,x2,y1,y2,r1,r2):
    assert Fraction(x1, x2) + Fraction (y1, y2) == Fraction(r1, r2)