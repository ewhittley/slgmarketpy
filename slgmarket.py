import slgproducts
import slgdiscounts
import slgbasketitems


def set_basket_discount_amount(product, discount, to_qty):
    if discount['amount'] is None:
        basket_discount_amount = str(-1 * float(product['price']) * to_qty)
    else:
        basket_discount_amount = str(-1 * float(discount['amount']))

    return basket_discount_amount


def compare_existing_discounts(product,
                               discount,
                               current_discounts,
                               current_qty):
    from_qty = int(discount['from_quantity'])
    to_qty = int(discount['to_quantity'])

    # magic math to compare discount defined quantities to existing
    # basket quantities and determine if a discount should be applied
    compare_existing = (from_qty + to_qty) * current_discounts
    compare_basket = current_qty - (from_qty + to_qty)

    if compare_existing == compare_basket:
        # either add the price of the discounted item or a specific
        # defined discount amount if it is declared

        discount_amount = set_basket_discount_amount(product, discount, to_qty)

        return discount_amount


def apply_available_discounts(product,
                              available_discounts,
                              current_discounts,
                              current_qty):
    basketitem = slgbasketitems.BasketItem()

    for discount in available_discounts:
        # set limit to infinite if we don't find one
        limit = int(discount['limit']) if discount['limit'] else float('inf')

        if (limit > current_discounts):
            add_discount = compare_existing_discounts(product,
                                                      discount,
                                                      current_discounts,
                                                      current_qty)

            if add_discount:
                basketitem.add_basket_item(None, discount['code'], add_discount)


def get_basket_qty(current_basket_items, available_discounts, product_code):
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

    return current_basket_quantity


def add_product_to_basket(product_code):
    product = slgproducts.Product()
    discount = slgdiscounts.Discount()
    basketitem = slgbasketitems.BasketItem()

    # get product info to add to basket item
    # take the first product returned since we should only return one
    product_to_add = product.get_products(product_code)[0]

    # add product to basket
    basketitem.add_basket_item(product_code, None, product_to_add['price'])
    current_basket_items = basketitem.get_basket_items()

    # get available discounts that match the product we just added
    available_discounts = discount.get_discounts(product_code)

    current_qty = get_basket_qty(current_basket_items,
                                 available_discounts,
                                 product_code)

    # check if discounts already exist if there is a limit on them
    basket_item_discounts = []

    for discount in available_discounts:
        for item in current_basket_items:
            if item['discount_code'] == discount['code']:
                basket_item_discounts.append(discount)

    current_discounts = len(basket_item_discounts)

    # add the discount to the basket
    apply_available_discounts(product_to_add,
                              available_discounts,
                              current_discounts,
                              current_qty)


def total_basket(basket_items):
    basket_sum = sum(float(item['amount']) for item in basket_items)

    return basket_sum


if __name__ == "__main__":
    product = slgproducts.Product()
    discount = slgdiscounts.Discount()
    basketitem = slgbasketitems.BasketItem()
    printitems = slgprinter.Printer()

    help_message = "COMMANDS: \nb = basket, p = product\n" \
                   "- b.add\n- p.add\n- help\n- stop"
    print(help_message)

    basket_items = basketitem.get_basket_items()
    printitems.print_basket(basket_items, total_basket(basket_items))

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
            printitems.print_basket(basket_items, total_basket(basket_items))
        elif "p.add" in action:
            product_code = raw_input("Enter the Product Code to add: ")
            product_name = raw_input("Enter the Product's Name: ")
            product_price = raw_input("Enter the Product's Price: ")

            product.add_product(product_code, product_name, product_price)

            product.get_products()
        else:
            print("That action is not valid.")
            basket_items = basketitem.get_basket_items()
            printitems.print_basket(basket_items, total_basket(basket_items))
