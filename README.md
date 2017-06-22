# README

This is a programming challenge to create a Farmer's market ordering system. The application will take orders into a basket and automatically add discounts where applicable.

## Setup

### Versions

* Python 2.7

## Running

From terminal run:
```
python slgmarket.py
```

Optional commands will be presented. Main command for the application is:
```
b.add
```
Which is short for basket.add. It will ask you for a product code, which must match the products in the list.

You can add more products using the command:
```
p.add
```

As you add products to the basket, the price will be totaled and discounts will automatically be applied where appropriate.

## Tests

Uses the Python **unittest** package

You can run tests with the following in terminal:
```
python test_slgmarket.py
```

## Current

There is currently 3 passing tests and 1 failing test. The failing test is for the CHMK discount. 
I need to rewrite the current_basket_quantity to include products for the from quantity. The reason the others pass right now is because the from and to products on the discount are the same product.

## Future

* The product add needs to be cleaned up
* Add the ability to update products and discounts
* Add the ability to destroy products and discounts