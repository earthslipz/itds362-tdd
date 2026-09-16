# Test list:
# [x] 200 g x 3 = 600 g
# [x] multiplying a quantity does not modify the original
# [x] two quantities with the same amount and unit are equal
# [x] 1 oz is not the same as 1 g
# [x] 200 g + 300 g = 500 g
# [x] 200 g + 1 oz, reduced to grams, using a conversion rate
# [x] (200 g + 1 oz) x 2

from kitchen import Quantity, Converter


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def test_multiplication():
    flour = grams(200)
    result = flour.times(3)
    assert result.amount == 600


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_addition_with_different_units():
    total = grams(200).plus(ounces(1))
    converter = Converter({"oz": 28.0})
    assert converter.reduce(total, "g") == grams(228)


def test_multiply_sum():
    total = grams(200).plus(ounces(1))
    converter = Converter({"oz": 28.0})
    doubled = total.times(2)
    assert converter.reduce(doubled, "g") == grams(456)
