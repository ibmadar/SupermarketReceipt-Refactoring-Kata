from enum import Enum


class Product:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def __str__(self):
        return f"{self.name} (units:{self.unit.name.lower()})"


class ProductUnit(Enum):
    EACH = 1
    KILO = 2


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4

class Offer:
    def __init__(self, offer_type, product, argument=None):
        self.offer_type = offer_type
        self.product = product

    def __str__(self):
        return f"\n{self.offer_type.name.lower()} {self.product.name}"
    
    def calculate_discount(self, unit_price, quantity):
        raise NotImplementedError("Subclasses should implement this!")
        
class Ten_percent_offer(Offer):
    def __init__(self, product, discount):
        super().__init__(SpecialOfferType.TEN_PERCENT_DISCOUNT, product)
        self.discount = discount

    def __str__(self):
        return f"\n{self.offer_type.name.lower()} {self.product.name} {self.discount}%"

    def calculate_discount(self, unit_price, quantity):
        return Discount(self.product, str(self.discount) + "% off", -quantity * unit_price * self.discount / 100.0)    


class Units_for_amount(Offer):
    def __init__(self, offertype, product, units, amount):
        super().__init__(offertype, product)
        self.amount = amount
        self.units = units

    def calculate_discount(self, unit_price, quantity):
        discount_n = unit_price * quantity - (quantity // self.units) * self.amount - (quantity % self.units) * unit_price
        
        return Discount(self.product, f"Buy {self.units} for ${self.amount}", -discount_n)

    def __str__(self):
        return f"\n{self.offer_type.name.lower()} {self.product.name} ${self.argument}"

class Five_for_amount_offer(Units_for_amount):
    def __init__(self, product, amount):
        super().__init__(SpecialOfferType.FIVE_FOR_AMOUNT, product, 5, amount)

class Two_for_amount_offer(Units_for_amount):
    def __init__(self, product, amount):
        super().__init__(SpecialOfferType.TWO_FOR_AMOUNT, product, 2, amount)
        
    
class Three_for_two_offer(Offer):
    def __init__(self, product):
        super().__init__(SpecialOfferType.THREE_FOR_TWO, product)

    def calculate_discount(self, unit_price, quantity):
        discount_n = unit_price * quantity - (quantity // 3) * unit_price * 2

        return Discount(self.product, f"Buy 3 for ${unit_price * 2}", -discount_n)
    
    def __str__(self):
        return f"\n{self.offer_type.name.lower()} {self.product.name}"    




class Discount:
    def __init__(self, product, description, discount_amount):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount

    def __str__(self):
        return f" Discount: Prod:{self.product} [Desc:{self.description}  Disc. Amount:{str(self.discount_amount)}]"


class OfferFactory:
    @staticmethod
    def create_offer(offer_type, product, argument):
        match offer_type:
            case SpecialOfferType.THREE_FOR_TWO:
                return Three_for_two_offer(product)
            case SpecialOfferType.TEN_PERCENT_DISCOUNT:
                return Ten_percent_offer(product, argument)
            case SpecialOfferType.TWO_FOR_AMOUNT:
                return Two_for_amount_offer(product, argument)
            case SpecialOfferType.FIVE_FOR_AMOUNT:
                return Five_for_amount_offer(product, argument) 
            case _:
                raise ValueError("Unknown offer type")