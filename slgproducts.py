import json_helper


class Product(object):

    def add_product(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

        product_data = {
            'code': self.code,
            'name': self.name,
            'price': self.price
            }

        json_helper.write_list('products.json', 'products', product_data)

    def update_product(self, code, name=None, price=None):
        pass

    def get_products(self, code=None):
        products = json_helper.get_list('products.json', 'code', code)

        return products
