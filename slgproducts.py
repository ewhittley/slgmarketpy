import json_helper


class Product(object):

    def add_product(self, code, name, price):
        product_data = {
            'code': code,
            'name': name,
            'price': price
            }

        json_helper.write_list('products.json', 'products', product_data)

    def get_products(self, code=None):
        products = json_helper.get_list('products.json', 'code', code)

        return products
