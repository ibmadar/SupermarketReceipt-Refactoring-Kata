from enum import Enum


class Product:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def __str__(self):
        return self.name + " " + self.unit.name.lower()


class ProductQuantity:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class ProductUnit(Enum):
    EACH = 1
    KILO = 2


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4

class Offer:
    def __init__(self, offer_type, product, argument):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument

    def __str__(self):
        return self.offer_type.name.lower() + " " + self.product.name + " " + str(self.argument) + "\n"
        


class Discount:
    def __init__(self, product, description, discount_amount):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount

    def __str__(self):
        return self.description + " " + str(self.discount_amount)
