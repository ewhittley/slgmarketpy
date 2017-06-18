import errno
import json
import json_helper


class Product(object):

	def add_product(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price

		product_data = {
						'code' : self.code,
						'name' : self.name,
						'price' : self.price
						}

		json_helper.write_list('products.json', 'products', product_data)


	def update_product(self, code, name=None, price=None):
		pass


	def get_products(self, code=None):
		products = json_helper.get_list('products.json', 'code', code)

		return products


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

		discount_data = {
							'code' : self.code,
							'description' : self.description,
							'limit' : self.limit,
							'from_product' : self.from_product,
							'from_quantity' : self.from_quantity,
							'to_product' : self.to_product,
							'to_quantity' : self.to_quantity,
							'amount' : self.amount
							}

		json_helper.write_list('discounts.json', 'discounts', discount_data)


	def update_discount(self):
		pass


	def get_discounts(self, product_code=None):
		with open('discounts.json', 'r') as discounts_file:
			discounts = json.load(discounts_file)

			from_discount = []
			to_discount = []

			if product_code is not None:
				for discount in discounts.values()[0]:
					if discount['from_product'] == product_code:
						from_discount.append(discount)
					if discount['to_product'] == product_code:
						to_discount.append(discount)

				# need to handle duplicate returns on discounts.
				# example: BOGO
				if from_discount == to_discount:
					return from_discount
				else:
					if from_discount:
						return from_discount
					elif to_discount:
						return to_discount
			else:
				print(discounts)


class BasketItem(object):

	def add_basket_item(self, product_code=None, 
						discount_code=None, amount=None):
		self.product_code = product_code
		self.discount_code = discount_code
		self.amount = amount

		basketitem_data = {
							'product_code' : self.product_code,
							'discount_code' : self.discount_code,
							'amount' : self.amount
							}

		json_helper.write_list('basketitems.json', 'basketitems', basketitem_data)


	def update_basket_item(self):
		pass


	def get_basket_items(self, product=None):
		basket_items = json_helper.get_list('basketitems.json')

		return basket_items

	def destroy_basket_items(self, product=None):
		with open('basketitems.json', 'r+') as basketitems_file:
			basketitems = json.load(basketitems_file)
			del basketitems['basketitems'][:]
			
			basketitems_file.seek(0)
			json.dump(basketitems, basketitems_file)
			basketitems_file.truncate()


def add_product_to_basket(product_code):
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	product_to_add = product.get_products(product_code)
	print("Adding to basket: {product}".format(product=product_to_add))

	basketitem.add_basket_item(product_to_add['code'], None, product_to_add['price'])

	discount_to_add = discount.get_discounts(product_to_add['code'])
	print("Adding Discount: {discount}".format(discount=discount_to_add))

	# basket_items = basketitem.get_basket_items()
	# discounts = get_discounts()


if __name__ == "__main__":
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	while True:
		action = raw_input("Type add.basket(CODE) or add.product or stop: ")
		if action == 'stop':
			basketitem.destroy_basket_items()
			break
		elif action == 'add.basket':
			add_product_to_basket('AP1')

			basket_items = basketitem.get_basket_items()
			print("Basket Items: {basket_items}".format(basket_items=basket_items))
		elif action == 'add.product':
			product.add_product(code, name, price)

			product.get_products()
		else:
			print("That action is not valid.")