class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit):
        return self

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, unit):
        amount = self.left.amount + self.right.amount
        return Quantity(amount, unit)


class Converter:
    def __init__(self, rates=None):
        self.rates = rates or {}

    def convert(self, quantity, unit):
        if quantity.unit == unit:
            return quantity
        rate = self.rates.get(quantity.unit)
        if rate is None:
            raise ValueError(f"No rate for {quantity.unit}")
        if unit == "g":
            return Quantity(quantity.amount * rate, "g")
        else:
            raise ValueError(f"Unsupported conversion to {unit}")

    def reduce(self, source, unit):
        if isinstance(source, Quantity):
            return self.convert(source, unit)
        if isinstance(source, Sum):
            left = self.reduce(source.left, unit)
            right = self.reduce(source.right, unit)
            return Quantity(left.amount + right.amount, unit)
        raise TypeError("Unknown source type")
