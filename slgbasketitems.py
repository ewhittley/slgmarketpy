import json
import json_helper


class BasketItem(object):

    def add_basket_item(self, product_code=None,
                        discount_code=None, amount=None):
        basketitem_data = {
            'product_code': product_code,
            'discount_code': discount_code,
            'amount': amount
            }

        json_helper.write_list('basketitems.json',
                               'basketitems',
                               basketitem_data)

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
