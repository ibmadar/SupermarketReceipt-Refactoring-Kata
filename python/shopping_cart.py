import math

from model_objects import SpecialOfferType, Discount


class ShoppingCart:

    def __init__(self):
        self._items = {}

    @property
    def items(self):
        return self._items.items()

    def add_item(self, product, quantity=1):
        self._items[product] = self._items.get(product,0) + quantity

    



                
