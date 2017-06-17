import pickle
import errno
import json


class Product(object):

	def add_product(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price

		product_data = {
										'code' : self.code,
										'name' : self.name,
										'price' : self.price}

		with open('products.json', 'r+') as products_file:
			products = json.load(products_file)
			products['products'].append(product_data)
			
			products_file.seek(0)
			json.dump(products, products_file)
			products_file.truncate()


	def update_product(self, code, name=None, price=None):
		pass


	def get_products(self, code=None):
		with open('products.json', 'r') as products_file:
			products = json.load(products_file)
			print(products)


class Discount(object):

	def add_discount(self, code, description, limit=None, 
					from_product=None, from_quantity=None, 
					to_product=None, to_quantity=None, amount=None):
		self.code = code
		self.description = description
		self.limit = limit
		self.from_product = from_product
		self.from_quantity = from_quantity
		self.to_product = to_product
		self.to_quantity = to_quantity
		self.amount = amount

		discount_data = {'code' : self.code,
							'description' : self.description,
							'limit' : self.limit,
							'from_product' : self.from_product,
							'from_quantity' : self.from_quantity,
							'to_product' : self.to_product,
							'to_quantity' : self.to_quantity,
							'amount' : self.amount}

		with open('discounts.json', 'r+') as discounts_file:
			discounts = json.load(discounts_file)
			discounts['discounts'].append(discount_data)
			
			discounts_file.seek(0)
			json.dump(discounts, discounts_file)
			discounts_file.truncate()


	def update_discount(self):
		pass


	def get_discounts(self, from_product=None, from_quantity=None, 
						to_product=None, to_quantity=None):
		with open('discounts.json', 'r') as discounts_file:
			discounts = json.load(discounts_file)
			print(discounts)


class BasketItem(object):

	def add_basket_item(self, product_code=None, discount_code=None, amount=None):
		self.product_code = product_code
		self.discount_code = discount_code
		self.amount = amount

		basketitem_data = {'product_code' : self.product_code,
							'discount_code' : self.discount_code,
							'amount' : self.amount}

		with open('basketitems.json', 'r+') as basketitems_file:
			basketitems = json.load(products_file)
			basketitems['basketitems'].append(basketitem_data)
			
			basketitems_file.seek(0)
			json.dump(basketitems, basketitems_file)
			basketitems_file.truncate()


	def update_basket_item(self):
		pass


	def get_basket_items(self, product=None):
		with open('basketitems.json', 'r') as basketitems_file:
			basketitems = json.load(basketitems_file)
			print(basketitems)


def add_product_to_basket(product_code):
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	product_to_add = product.get_products(product_code)

	basket_items = basketitem.get_basket_items()
	discounts = get_discounts()


	


if __name__ == "__main__":
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	# basket_item.add_basket_item()

	basketitem.get_basket_items()

	action = raw_input("What would you like to do?\n- Add Product\n- Add Basket Item\n")

	if action == "Add Product":
		code = raw_input("Enter the Product Code: ")
		name = raw_input("Enter the Product Name: ")
		price = raw_input("Enter the Product Price: ")

		# product = Product(code, name, price)
		product.add_product(code, name, price)

		product.get_products()