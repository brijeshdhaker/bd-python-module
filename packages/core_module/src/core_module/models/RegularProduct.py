
# The Traditional Way (With Boilerplate)
class RegularProduct:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"RegularProduct(name={self.name!r}, price={self.price}, quantity={self.quantity})"