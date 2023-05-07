class Inventory:
    def __init__(self):
        self.stock = {} # انبار به صورت آیدی کالا و موجودی.


    def display_menu(self):
        up = int(input("What do you want to do?\nEnter 0 to back to admin menu.\nEnter 1 for Update the inventory with csv file.\nEnter 2 for Update the inventory with normal input.\nEnter 3 to see inventory.\nEnter 4 to add items.\n"))

        if up == 0:
            return 0

        if up == 1:
            return 1

        elif up == 2:
            return 2

        elif up == 3:
            return 3

        elif up == 4:
            return 4

    def update_stock(self, item_code, quantity): #متود آپدیت انبار به صورت ورودی
        if item_code in self.stock:
            self.stock[item_code] = quantity
        else:
            self.stock[item_code] = quantity

    def get_stock(self):
        return self.stock

    def save_stock(self, filename):              #متود ذخیره آیتم ها داخل فایل csv یا txt
        with open(filename, 'w') as f:
            for item_code, quantity in self.stock.items():
                f.write(f"{item_code},{quantity},1\n")

    def load_stock(self, filename):              #متود لود کردن آیتم ها از روی فایلcsv
        with open(filename, 'r') as f:
            for line in f:
                item_code, quantity = line.strip().split(',')
                self.stock[item_code] = int(quantity)

    def add_item(self, item_code, quantity):    #متود اضافه کردن آیتم به صورت دستی
        self.stock[item_code] = quantity

inventory = Inventory()
inventory.load_stock('موجودی اولیه.csv')

def display():

    while True:
        display_menu = inventory.display_menu()
        if display_menu == 0:
            return 0

        elif display_menu == 1:
            return 1

        elif display_menu == 2:
            return 2

        elif display_menu == 3:
            return 3

        elif display_menu == 4:
            return 4



        inventory.save_stock('inventory.csv')
        inventory.save_stock('inventory.txt')
