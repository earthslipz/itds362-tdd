# Test list:
# [x] 200 g x 3 = 600 g
# [x] multiplying a quantity does not modify the original
# [ ] two quantities with the same amount and unit are equal
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz, reduced to grams, using a conversion rate
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    result = flour.times(3)
    assert result.amount == 600


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)


def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
