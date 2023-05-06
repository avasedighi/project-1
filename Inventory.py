class Inventory:
    def __init__(self):
        self.stock = {}


    def display_menu(self):
        up = int(input("What do you want to do?\nEnter 0 for exit.\nEnter 1 for Update the inventory with csv file.\nEnter 2 for Update the inventory with normal input.\nEnter 3 to see inventory.\nEnter 4 to add items.\n"))

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

    def get_stock(self):
        return self.stock

    def save_stock(self, filename):
        with open(filename, 'w') as f:
            for item_code, quantity in self.stock.items():
                f.write(f"{item_code},{quantity},1\n")

    def load_stock(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                item_code, quantity = line.strip().split(',')
                self.stock[item_code] = int(quantity)

    def add_item(self, item_code, quantity):
        self.stock[item_code] = quantity

inventory = Inventory()
inventory.load_stock('موجودی اولیه.csv')
while True:
    display_menu = inventory.display_menu()
    if display_menu == 0:
        exit(0)

    elif display_menu == 1:
        r = input(("Enter the csv file address\n"))
        inventory.load_stock(r)

    elif display_menu == 2:
        contin = "Y"
        while contin == "Y":
            item = input("Please enter the item code.\n")
            quantity = int(input("Please enter the new quantity.\n"))
            inventory.update_stock(item ,quantity)
            contin = input("do you want update the other items?\nEnter Y for yes. N for n.")

    elif display_menu == 3:
        m = input("If you want the inventory file as CSV file enter C. Else enter T.\n")
        if m == "C":
            inventory.save_stock('inventory.csv')
            print("you can check the 'inventory.csv' file.")

        elif m == "T":
            inventory.save_stock('inventory.txt')
            print("you can check the 'inventory.txt'")

    elif display_menu == 4:
        t = input("Enter the item title:\n")
        i = input("Enter the item ID:\n")
        q = int(input("Enter the quantity:\n"))
        p = float(input("Enter the price:\n"))
        pic = int(input("Enter the lego pieces:\n"))
        age = input("Enter the ege rate:\n")
        it = int(input("Enter the item:\n"))

        inventory.add_item(i, q)

    inventory.save_stock('inventory.csv')
    inventory.save_stock('inventory.txt')
