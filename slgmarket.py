import pickle


class Product(object):

	def __init__(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price


	def add_product(self):
		product_data = {'code' : self.code,
						'name' : self.name,
						'price' : self.price}

		pickle_file = open('product.pkl', 'wb')

		pickle.dump(product_data, pickle_file)

		pickle_file.close()

	def update_product(self):
		pass

	def get_product(self, code=None):
		pickle_file = open('product.pkl', 'rb')

		pickle_data = pickle.load(pickle_file)

		print(pickle_file)

		pickle_file.close()


class Discount(object):

	def __init__(self, code, description, limit=None, 
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

	def add_discount(self):
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

		print(pickle_file)

		pickle_file.close()


if __name__ == "__main__":
	action = raw_input("What would you like to do?\n- Add Product\n- Add Basket Item\n")

	if action == "Add Product":
		code = raw_input("Enter the Product Code: ")
		name = raw_input("Enter the Product Name: ")
		price = raw_input("Enter the Product Price: ")

		product = Product(code, name, price)

		product.add_product()

		product.get_product()