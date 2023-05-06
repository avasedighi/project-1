class Inventory:
    def __init__(self):
        self.stock = {}


    def display_menu(self):
        up = int(input("What do you want to do?\nEnter 1 for Update the inventory with csv file\nEnter 2 for Update the inventory with normal input\nEnter 3 to see inventory.\n"))
        if up == 1:
            return 1

        elif up == 2:
            return 2

        elif up == 3:
            return 3

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

inventory = Inventory()
inventory.load_stock('موجودی اولیه.csv')
display_menu = inventory.display_menu()

if display_menu == 1:
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

inventory.save_stock('inventory.csv')
inventory.save_stock('inventory.txt')
