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
		discounts = json_helper.get_list('discounts.json', 'from_product', product_code)

		return discounts


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


def apply_available_discounts(product, available_discounts, current_discounts, current_basket_quantity):
	for discount in available_discounts:
		# set limit to infinite if we don't find one
		limit = int(discount['limit']) if discount['limit'] else float('inf')
		if (limit > current_discounts):
			from_qty = int(discount['from_quantity'])
			to_qty = int(discount['to_quantity'])

			# magic math to compare discount defined quantities to existing
			# basket quantities and determine if a discount should be applied
			compare_existing = (from_qty + to_qty) * current_discounts
			compare_basket = current_basket_quantity - (from_qty + to_qty)

			if compare_existing == compare_basket:
				# either add the price of the discounted item or a specific defined
				# discount amount if it is declared
				if discount['amount'] is None:
					basket_discount_amount = float(product['price']) * to_qty

					basketitem.add_basket_item(None, discount['code'], basket_discount_amount)
				else:
					basketitem.add_basket_item(None, discount['code'], discount['amount'])


def add_product_to_basket(product_code):
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	# get product info to add to basket item
	# take the first product returned since we should only return one
	product_to_add = product.get_products(product_code)[0]

	# add product to basket
	basketitem.add_basket_item(product_code, None, product_to_add['price'])
	current_basket_items = basketitem.get_basket_items()

	# get available discounts that match the product we just added
	available_discounts = discount.get_discounts(product_code)

	# find total number of same products in basket now
	# used to match against discount quantity
	basket_matches = []

	for item in current_basket_items:
		if item['product_code'] == product_code:
			basket_matches.append(item)

	current_basket_quantity = len(basket_matches)
	
	# check if discounts already exist if there is a limit on them
	basket_item_discounts = []

	for discount in available_discounts:
		for item in current_basket_items:
			if item['discount_code'] == discount['code']:
				basket_item_discounts.append(discount)

	current_discounts = len(basket_item_discounts)

	# add the discount to the basket
	apply_available_discounts(product_to_add, available_discounts, current_discounts, current_basket_quantity)


def checkout_print(basket_items):
	header = "Item             Price  \n------------------------"

	print_list = []

	print_list.append(header)

	for item in basket_items:
		if item['product_code']:
			price_spacing = " " * (11 - len(str(item['amount'])))
			item_line = "{code}         {spacing}{amount}".format(code=item['product_code'], 
																	spacing=price_spacing,
																	amount=item['amount'])
			print_list.append(item_line)
		elif item['discount_code']:
			print(item['amount'])
			price_spacing = " " * (10 - len(str(item['amount'])))
			item_line = "      {discount}  {spacing}-{amount}".format(discount=item['discount_code'],
																		spacing=price_spacing,
																		amount=item['amount'])
			print_list.append(item_line)
		else:
			# something weird here, we have a product and
			# discount on the same line
			raise

	for print_line in print_list:
		print(print_line)



if __name__ == "__main__":
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	help_message = "COMMANDS: \nb = basket, p = product\n- b.add\n- p.add\n- help\n- stop"
	print(help_message)

	basket_items = basketitem.get_basket_items()
	checkout_print(basket_items)

	while True:
		action = raw_input("action: ")
		if action == 'stop':
			basketitem.destroy_basket_items()
			break
		elif action == 'help':
			print(help_message)
		elif "b.add" in action:
			product_code = raw_input("Enter the Product Code to scan: ")
			
			add_product_to_basket(product_code)

			basket_items = basketitem.get_basket_items()
			checkout_print(basket_items)
		elif "p.add" in action:
			product_code = raw_input("Enter the Product Code to add: ")
			product_name = raw_input("Enter the Product's Name: ")
			product_price = raw_input("Enter the Product's Price: ")

			product.add_product(product_code, product_name, product_price)

			product.get_products()
		else:
			print("That action is not valid.")
			basket_items = basketitem.get_basket_items()
			checkout_print(basket_items)