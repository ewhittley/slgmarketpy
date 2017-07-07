import json_helper


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
        discounts = json_helper.get_list('discounts.json', 'to_product', product_code)

        return discounts
