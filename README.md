# README

This is a programming challenge to create a Farmer's market ordering system. The application will take orders into a basket and automatically add discounts where applicable.

## Setup

### Versions

* Python 2.7

## Running

Set up virtualenv
```
virtualenv --python=/usr/bin/python2.7
```

Activate the virtualenv
```
source slgmarketpy/bin/activate
```

* Note: there are no additionally required packages with this script

Run the slgmarket script
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
