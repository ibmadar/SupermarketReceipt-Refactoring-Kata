import pytest
import approvaltests

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog


def test_regular_shopping():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 0.99)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)

   
    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)

def test_ten_percent_discount():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 0.99)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)

    #Add offers
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)


def test_same_item__added_multiple_times():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 0.99)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)

    #Add offers
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(apples, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)    

def test_no_offers():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 0.99)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)


    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)    


def test_3x2_discount():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 2)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)

    #Add offers
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush)

    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(toothbrush, 3)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)    


def test_2_for_amount_discount():
    catalog = FakeCatalog()

    #Products
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    #Add them to catalog
    catalog.add_product(toothbrush, 2)    
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)

    #Add offers
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, toothbrush,1.5)

    #Shopping cart
    cart = ShoppingCart()
    cart.add_item(apples, 2.5)
    cart.add_item(toothbrush, 3)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(receipt)        