import unittest
import slgmarket
import slgbasketitems


class BasketItemsTester(unittest.TestCase):

    def test_chmk_discount(self):
        basketitem = slgbasketitems.BasketItem()

        products = ['CH1', 'AP1', 'CF1', 'MK1']

        for product in products:
            slgmarket.add_product_to_basket(product)

        basket_items = basketitem.get_basket_items()
        # print(self.basket_items)

        total = slgmarket.total_basket(basket_items)

        basketitem.destroy_basket_items()

        self.assertEqual(total, 20.34)

    def test_no_discount(self):
        basketitem = slgbasketitems.BasketItem()

        products = ['MK1', 'AP1']

        for product in products:
            slgmarket.add_product_to_basket(product)

        basket_items = basketitem.get_basket_items()
        # print(self.basket_items)

        total = slgmarket.total_basket(basket_items)

        basketitem.destroy_basket_items()

        self.assertEqual(total, 10.75)

    def test_bogo_discount(self):
        basketitem = slgbasketitems.BasketItem()

        products = ['CF1', 'CF1']

        for product in products:
            slgmarket.add_product_to_basket(product)

        basket_items = basketitem.get_basket_items()
        # print(self.basket_items)

        total = slgmarket.total_basket(basket_items)

        basketitem.destroy_basket_items()

        self.assertEqual(total, 11.23)

    def test_appl_discount(self):
        basketitem = slgbasketitems.BasketItem()

        products = ['AP1', 'AP1', 'CH1', 'AP1']

        for product in products:
            slgmarket.add_product_to_basket(product)

        basket_items = basketitem.get_basket_items()
        # print(self.basket_items)

        total = slgmarket.total_basket(basket_items)

        basketitem.destroy_basket_items()

        self.assertEqual(total, 16.61)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
