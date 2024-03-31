from model_objects import Offer, OfferFactory
from receipt import Receipt


class Teller:

    def __init__(self, catalog):
        self.catalog = catalog
        self.offers = {}

    
    def add_special_offer(self, offer_type, product, argument=None):
        self.offers[product] = OfferFactory.create_offer(offer_type, product, argument)

    def checks_out_articles_from(self, the_cart):
        receipt = Receipt()
        for prod, quantity in the_cart.items:
            unit_price = self.catalog.unit_price(prod)
            receipt.add_product(prod, quantity, unit_price)
            offer = self.offers.get(prod,None)
            if offer:
                receipt.add_discount(offer.calculate_discount(unit_price, quantity))
        return receipt

    
