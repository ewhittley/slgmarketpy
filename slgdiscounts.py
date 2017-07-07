import json_helper


class Discount(object):

    def add_discount(self, code, description, limit=None,
                     from_product=None, from_quantity=None,
                     to_product=None, to_quantity=None, amount=None):
        discount_data = {
            'code': code,
            'description': description,
            'limit': limit,
            'from_product': from_product,
            'from_quantity': from_quantity,
            'to_product': to_product,
            'to_quantity': to_quantity,
            'amount': amount
            }

        json_helper.write_list('discounts.json', 'discounts', discount_data)

    def get_discounts(self, product_code=None):
        discounts = json_helper.get_list('discounts.json', 'to_product',
                                         product_code)

        return discounts
