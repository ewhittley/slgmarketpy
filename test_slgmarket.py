import unittest
import slgmarket


class BasketItemsTester(unittest.TestCase):

	def test_chai_discount(self):
		self.basketitem = slgmarket.BasketItem()

		self.products = ['CH1', 'AP1', 'CF1', 'MK1']

		for product in self.products:
			slgmarket.add_product_to_basket(product)

		self.basket_items = self.basketitem.get_basket_items()
		# print(self.basket_items)

		self.total = slgmarket.total_basket(self.basket_items)

		self.basketitem.destroy_basket_items()

		self.assertEqual(self.total, 20.34)


	def test_no_discount(self):
		self.basketitem = slgmarket.BasketItem()

		self.products = ['MK1', 'AP1']

		for product in self.products:
			slgmarket.add_product_to_basket(product)

		self.basket_items = self.basketitem.get_basket_items()
		# print(self.basket_items)

		self.total = slgmarket.total_basket(self.basket_items)

		self.basketitem.destroy_basket_items()

		self.assertEqual(self.total, 10.75)


	def test_coffee_discount(self):
		self.basketitem = slgmarket.BasketItem()

		self.products = ['CF1', 'CF1']

		for product in self.products:
			slgmarket.add_product_to_basket(product)

		self.basket_items = self.basketitem.get_basket_items()
		# print(self.basket_items)

		self.total = slgmarket.total_basket(self.basket_items)

		self.basketitem.destroy_basket_items()

		self.assertEqual(self.total, 11.23)


	def test_apple_discount(self):
		self.basketitem = slgmarket.BasketItem()

		self.products = ['AP1', 'AP1', 'CH1', 'AP1']

		for product in self.products:
			slgmarket.add_product_to_basket(product)

		self.basket_items = self.basketitem.get_basket_items()
		# print(self.basket_items)

		self.total = slgmarket.total_basket(self.basket_items)

		self.basketitem.destroy_basket_items()

		self.assertEqual(self.total, 16.61)


def main():
	unittest.main()


if __name__ == '__main__':
	main()
