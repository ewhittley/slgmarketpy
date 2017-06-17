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


if __name__ == "__main__":
	action = raw_input("What would you like to do?\n- Add Product\n- Add Basket Item\n")

	if action == "Add Product":
		code = raw_input("Enter the Product Code: ")
		name = raw_input("Enter the Product Name: ")
		price = raw_input("Enter the Product Price: ")

		product = Product(code, name, price)

		product.add_product()

		pickle_file = open('product.pkl', 'rb')

		pickle_data = pickle.load(pickle_file)

		print(pickle_data)

		pickle_file.close()