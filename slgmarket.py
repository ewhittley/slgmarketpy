import pickle
import errno


class Product(object):

	def add_product(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price

		product_data = {'code' : self.code,
						'name' : self.name,
						'price' : self.price}

		pickle_file = open('product.pkl', 'wb')

		pickle.dump(product_data, pickle_file)

		pickle_file.close()


	def update_product(self, code, name=None, price=None):
		pass


	def get_product(self, code=None):
		pickle_file = open('product.pkl', 'rb')

		pickle_data = pickle.load(pickle_file)

		print(pickle_data)

		pickle_file.close()


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

		pickle_file = open('discount.pkl', 'wb')

		pickle.dump(discount_data, pickle_file)

		pickle_file.close()


	def update_discount(self):
		pass


	def get_discount(self, code=None):
		pickle_file = open('discount.pkl', 'rb')

		pickle_data = pickle.load(pickle_file)

		print(pickle_data)

		pickle_file.close()

class BasketItem(object):

	def add_basket_item(self, product_code=None, discount_code=None, amount=None):
		self.product_code = product_code
		self.discount_code = discount_code
		self.amount = amount

		basket_item_data = {'product_code' : self.product_code,
							'discount_code' : self.discount_code,
							'amount' : self.amount}

		pickle_file = open('basket_item.pkl', 'wb')

		pickle.dump(basket_item_data, pickle_file)

		pickle_file.close()


	def update_basket_item(self):
		pass


	def get_basket_item(self):
		try:
			pickle_file = open('basket_item.pkl', 'rb')

			pickle_data = pickle.load(pickle_file)

			print(pickle_data)

			pickle_file.close()
		except IOError,e:
			if e[0] == errno.ENOENT:
				print("No Basket Items")
			else:
				raise


def add_product_to_basket(product_code):
	product = Product(product_code)
	product = BasketItem(product_code=product_code, )


if __name__ == "__main__":
	product = Product()
	discount = Discount()
	basketitem = BasketItem()

	# basket_item.add_basket_item()

	basket_item.get_basket_item()

	action = raw_input("What would you like to do?\n- Add Product\n- Add Basket Item\n")

	if action == "Add Product":
		code = raw_input("Enter the Product Code: ")
		name = raw_input("Enter the Product Name: ")
		price = raw_input("Enter the Product Price: ")

		# product = Product(code, name, price)
		product.add_product(code, name, price)

		product.get_product()