import json
class AccountingSystem:
    def __init__(self, quantity, order_number, net_price, shipping_cost):
        self.quantity = quantity
        self.order_number = order_number
        self.net_price = net_price
        self.shipping_cost = shipping_cost
        self.report = []

    def add_order(self):
        # محاسبه مالیات سفارش
        tax = self.net_price * 0.09

        # ایجاد دیکشنری برای خیره اطلاعات سفارش
        order = {
            'تعداد کالا': self.quantity,
            'شماره سفارش': self.order_number,
            'قیمت خالص': self.net_price,
            'هزینه ارسال': self.shipping_cost,
            'مالیات': tax
        }

        return order

def write(filename, report):
    with open(filename, 'w') as f:
        f.write(report)
#متاسفانه اینجا کدگذاری میکنه و اطلاعات فارسی رو نمیشه خوند. فقط عددا مشخصه.
def export(list):
    x = ""
    for i in list:
        x += json.dumps(i, indent=4)
    return x
