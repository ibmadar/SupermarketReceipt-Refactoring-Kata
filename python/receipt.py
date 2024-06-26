
class ReceiptItem:
    def __init__(self, product, quantity, price, total_price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_price = total_price

    def __str__(self):
        return f"Item: {self.product} - Qty:{self.quantity} - Unit price:{self.price} - Price:{self.total_price}"


class Receipt:
    def __init__(self):
        self._items = []
        self._discounts = []

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.total_price
        for discount in self.discounts:
            total += discount.discount_amount
        return total

    def add_product(self, product, quantity, price):
        total_price = quantity * price
        self._items.append(ReceiptItem(product, quantity, price, total_price))

    def add_discount(self, discount):
        self._discounts.append(discount)

    @property
    def items(self):
        return self._items[:]

    @property
    def discounts(self):
        return self._discounts[:]
    
    def __str__(self):
        result = "Receipt:\n"
        result += "\n".join(str(item) for item in self.items)
        result += "\n".join(str(disc) for disc in self.discounts)
        result += f"\nTotal: {self.total_price()}"
        return result
