class Printer(object):

    def print_header(self):
        item_header = "Item".ljust(3)
        discount_header = " " * 4
        price_header = "Price".rjust(16)

        header = "{item}{discount}{price}".format(item=item_header,
                                                  discount=discount_header,
                                                  price=price_header)

        return header

    def print_separator(self):
        line_separater = "-" * 24

    def print_line_item(self, basket_items):
        for item in basket_items:
            amount = "${:,.2f}".format(float(item['amount'])).rjust(12)

            if item['product_code']:
                item_line = "{code}         {amount}".format(code=item['product_code'],
                                                             amount=amount)
                return item_line
                # print_list.append(item_line)
            elif item['discount_code']:
                item_line = "      {discount}  {amount}".format(discount=item['discount_code'],
                                                                amount=amount)
                return item_line
                # print_list.append(item_line)
            else:
                # something weird here, we have a product and
                # discount on the same line
                raise

    def print_footer(self, total):
        total = "${:,.2f}".format(total).rjust(24)
        footer = "{total}".format(total=total)

        return footer

    def print_basket(self, basket_items, total):
        print_list = []

        print_list.append(self.print_header())
        print_list.append(self.print_separator())

        print_list.append(self.print_line_item(basket_items))

        print_list.append(self.print_footer(total))

        for print_line in print_list:
            print(print_line)
