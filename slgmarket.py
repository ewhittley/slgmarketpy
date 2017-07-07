import json
import json_helper
import unittest
import slgproducts
import slgdiscounts


class BasketItem(object):

    def add_basket_item(self, product_code=None,
                        discount_code=None, amount=None):
        self.product_code = product_code
        self.discount_code = discount_code
        self.amount = amount

        basketitem_data = {
            'product_code' : self.product_code,
            'discount_code' : self.discount_code,
            'amount' : self.amount
            }

        json_helper.write_list('basketitems.json', 'basketitems', basketitem_data)


    def update_basket_item(self):
        pass


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


def apply_available_discounts(product, available_discounts, current_discounts, current_basket_quantity):
    basketitem = BasketItem()

    for discount in available_discounts:
        # set limit to infinite if we don't find one
        limit = int(discount['limit']) if discount['limit'] else float('inf')

        if (limit > current_discounts):
            from_qty = int(discount['from_quantity'])
            to_qty = int(discount['to_quantity'])

            # magic math to compare discount defined quantities to existing
            # basket quantities and determine if a discount should be applied
            compare_existing = (from_qty + to_qty) * current_discounts
            compare_basket = current_basket_quantity - (from_qty + to_qty)

            if compare_existing == compare_basket:
                # either add the price of the discounted item or a specific defined
                # discount amount if it is declared
                if discount['amount'] is None:
                    basket_discount_amount = str(-1 * float(product['price']) * to_qty)

                    basketitem.add_basket_item(None, discount['code'], basket_discount_amount)
                else:
                    basket_discount_amount = str(-1 * float(discount['amount']))
                    basketitem.add_basket_item(None, discount['code'], basket_discount_amount)


def add_product_to_basket(product_code):
    product = slgproducts.Product()
    discount = slgdiscounts.Discount()
    basketitem = BasketItem()

    # get product info to add to basket item
    # take the first product returned since we should only return one
    product_to_add = product.get_products(product_code)[0]

    # add product to basket
    basketitem.add_basket_item(product_code, None, product_to_add['price'])
    current_basket_items = basketitem.get_basket_items()

    # get available discounts that match the product we just added
    available_discounts = discount.get_discounts(product_code)

    # find total number of same products in basket now
    # used to match against discount quantity
    basket_matches = []

    for item in current_basket_items:
        for discount in available_discounts:
            if item['product_code'] == product_code:
                basket_matches.append(item)
            elif item['product_code'] == discount['from_product']:
                basket_matches.append(item)

    current_basket_quantity = len(basket_matches)

    # check if discounts already exist if there is a limit on them
    basket_item_discounts = []

    for discount in available_discounts:
        for item in current_basket_items:
            if item['discount_code'] == discount['code']:
                basket_item_discounts.append(discount)

    current_discounts = len(basket_item_discounts)

    # add the discount to the basket
    apply_available_discounts(product_to_add, available_discounts, current_discounts, current_basket_quantity)


def total_basket(basket_items):
    basket_sum = sum(float(item['amount']) for item in basket_items)

    return basket_sum


def checkout_print(basket_items):
    print_list = []

    item_header = "Item".ljust(3)
    discount_header = " " * 4
    price_header = "Price".rjust(16)

    header = "{item}{discount}{price}".format(item=item_header,
                                                discount=discount_header,
                                                price=price_header)

    print_list.append(header)

    line_separater = "-" * 24
    print_list.append(line_separater)

    for item in basket_items:
        amount = "${:,.2f}".format(float(item['amount'])).rjust(12)
        if item['product_code']:
            item_line = "{code}         {amount}".format(code=item['product_code'],
                                                            amount=amount)
            print_list.append(item_line)
        elif item['discount_code']:
            item_line = "      {discount}  {amount}".format(discount=item['discount_code'],
                                                            amount=amount)
            print_list.append(item_line)
        else:
            # something weird here, we have a product and
            # discount on the same line
            raise

    print_list.append(line_separater)

    total = "${:,.2f}".format(total_basket(basket_items)).rjust(24)
    footer = "{total}".format(total=total)

    print_list.append(footer)

    for print_line in print_list:
        print(print_line)



if __name__ == "__main__":
    product = slgproducts.Product()
    discount = slgdiscounts.Discount()
    basketitem = BasketItem()

    help_message = "COMMANDS: \nb = basket, p = product\n- b.add\n- p.add\n- help\n- stop"
    print(help_message)

    basket_items = basketitem.get_basket_items()
    checkout_print(basket_items)

    while True:
        action = raw_input("action: ")
        if action == 'stop':
            basketitem.destroy_basket_items()
            break
        elif action == 'help':
            print(help_message)
        elif "b.add" in action:
            product_code = raw_input("Enter the Product Code to scan: ")

            add_product_to_basket(product_code)

            basket_items = basketitem.get_basket_items()
            checkout_print(basket_items)
        elif "p.add" in action:
            product_code = raw_input("Enter the Product Code to add: ")
            product_name = raw_input("Enter the Product's Name: ")
            product_price = raw_input("Enter the Product's Price: ")

            product.add_product(product_code, product_name, product_price)

            product.get_products()
        else:
            print("That action is not valid.")
            basket_items = basketitem.get_basket_items()
            checkout_print(basket_items)
