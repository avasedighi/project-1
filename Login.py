import random
from Address import Logistic
from Inventory import Inventory
from Accounting import AccountingSystem
from Inventory import display
from Accounting import export
from Accounting import write

inventory = Inventory()
inventory.load_stock('موجودی اولیه.csv')

class Lego:
    def __init__(self, title: str, price: float, pieces: int, ageRate: str,
                 item: int, stockCount: int, idCode: int):
        self.title = title
        self.price = price
        self.pieces = pieces
        self.ageRate = ageRate
        self.item = item
        self.stockCount = stockCount
        self.idCode = idCode


grand_piano_1 = Lego('Grand Piano', 399.99, 3662, 'A', 21323, 3, 101)
grand_piano_2 = Lego('Grand Piano', 249.99, 1780, 'B', 10562, 4, 102)
grand_piano_3 = Lego('Grand Piano', 99.99, 431, 'C', 1098, 0, 103)

eiffel_tower_1 = Lego('Eiffel Tower', 629.99, 10001, 'A', 1098, 10, 201)
eiffel_tower_2 = Lego('Eiffel Tower', 539.99, 8893, 'B', 850, 0, 202)
eiffel_tower_3 = Lego('Eiffel Tower', 349.99, 1087, 'C', 460, 4, 203)

car_1 = Lego('porsche', 290.99, 2308, 'A', 10295, 17, 301)
car_2 = Lego('porsche', 169.99, 1458, 'B', 4056, 29, 302)
car_3 = Lego('porsche', 89.99, 560, 'C', 1105, 27, 303)

house_1 = Lego('House', 89.99, 3101, 'A', 7089, 23, 401)
house_2 = Lego('House', 89.99, 1780, 'B', 4178, 30, 402)
house_3 = Lego('House', 44.99, 604, 'C', 1056, 16, 403)

stuff = [grand_piano_1, grand_piano_2, grand_piano_3, house_1, house_2, house_3,
         eiffel_tower_1, eiffel_tower_2, eiffel_tower_3, car_1, car_2, car_3]

Users = {}

Admins = {'Ava': '1234', 'Nima': '1234', 'Sadra': '1234'}
report = []
shopping_bag = {}
def checkout(lego, n, username):
    print(f"{lego.price} * {n} + 5 (delivery) = {lego.price * n + 5} dollars.")
    cardNumber = input("Enter your credit card number: ")
    if len(cardNumber) == 16:
        print("Checked out succesfully.")
        lego.stockCount = lego.stockCount - n
        inventory.stock[str(lego.idCode)] = lego.stockCount
        shopping_bag[username] = []
        order_number = random.randint(10**16 , 10**17 - 1)
        report.append(AccountingSystem(n, order_number, n * lego.price, 5).add_order())
        print(report)

        mainMenu(username)

    else:
        print("EROR! try again for checking out.")
        checkout(lego, n, username)


def howMany(lego, username):
    n = 1
    n = int(input(f"How many {lego.title} do you want? (up to {lego.stockCount})"))
    if n > lego.stockCount:
        print(f"Up to {lego.stockCount} please!")
        howMany(lego, username)
    return n


def buying(lego, username):
    shopping_bag[username].append(lego)
    print("Ok, this lego is in your bag. Type 'shop' to continue shopping")
    print("Type 'next' to checkout and type 'menu' to back to menu.")
    x = input()
    if x == 'shop':
        shop(username)
    elif x == 'next':
        n = howMany(lego, username)
        # Creating an instance of the Logistic class
        logistic = Logistic()

        while True:

            # Displaying the address menu for the user to enter their details
            logistic.display_address_menu()

            # Selecting the delivery method based on the user's county
            logistic.delivery_method()

            # Selecting the delivery time based on available capacity
            logistic.delivery_time()

            # Confirming the entered details with the user
            confirmed = logistic.confirmation()

            # If the user confirms the entered details, print the address
            if confirmed:
                print("Address confirmed.")
                checkout(lego, n, username)
                break
            else:
                print("Address not confirmed. Please try again.")


    elif x == 'menu':
        mainMenu(username)
    else:
        print("Enter a valid command please!")
        print("")
        buying(lego, username)


def showDetailes(x, age_range, username):
    tru = 0
    for i in stuff:
        if x == str(i.idCode):
            print(f"This Lego has {i.pieces} pieces and {i.item} items. All of these ONLY {i.price} $!")
            buy = input("Type 'add' to add this Lego to your bag and type 'back' to back to other Legos. ")
            if buy == 'add':
                buying(i, username)
                tru = 1
            elif buy == 'back':
                showAvailable(age_range, username)
                tru = 1
            break

    if tru == 0:
        print("we don't have any Lego with this code. please enter the id code more carefully.")
        showAvailable(age_range, username)


def showAvailable(age_range, username):
    print("")
    print("These products are available:")
    print("")
    for i in stuff:
        if i.stockCount > 0 and i.ageRate == age_range:
            print(i.title, i.idCode)
            print(i.price, '$')
            print("")
        if i.stockCount <= 0 and i.ageRate == age_range:
            print(i.title, i.idCode)
            print('Unavailable')
            print("")

    x = input("Type the id code of each Lego to see more details or type 'back' to back to menu. ")
    if x == 'back':
        mainMenu(username)
    else:
        showDetailes(x, age_range, username)


def shop(username):
    print("Choose an age range to find your Lego. (A: 18-85, B: 12-18, C: 7-12)")
    print("Type 'menu' to back to menu.")
    x = input()
    if x == 'A' or x == 'a':
        showAvailable('A', username)

    elif x == 'B' or x == 'b':
        showAvailable('B', username)

    elif x == 'C' or x == 'b':
        showAvailable('C', username)

    else:
        print("Enter a valid command.")
        shop(username)


def adminMenu(admin):
    print("Type 'accounting' to export the accounting file.")
    print("Type 'inventory' to do inventory management.")
    print("Type log out to log out.")
    x = input()

    if x == 'accounting' or x == 'Accounting':
        write("report.csv",export(report))
        write("report.txt",export(report))

        adminMenu(admin)

    elif x == 'inventory' or x == 'Inventory':
        print(inventory.stock)
        d = display()
        if d == 0:
            adminMenu(admin)

        if d == 1:
            r = input(("Enter the csv file address\n"))
            inventory.load_stock(r)
            with open(r, 'r') as f:
                for line in f:
                    item_code, quantity = line.strip().split(',')
                    for i in stuff:
                        if i.idCode == int(item_code):
                            i.stockCount = quantity

            print("Inventory Update was successful.")
            adminMenu(admin)

        if d == 2:
            contin = "Y"
            while contin == "Y":
                item = int(input("Please enter the item code.\n"))
                quantity = int(input("Please enter the new quantity.\n"))
                inventory.update_stock(str(item), quantity)
                for i in stuff:
                    if i.idCode == item:
                        i.stockCount = quantity

                contin = input("do you want update the other items?\nEnter Y for yes. N for n.")

            adminMenu(admin)

        elif d == 3:
            m = input("If you want the inventory file as CSV file enter C. Else enter T.\n")
            if m == "C":
                inventory.save_stock('inventory.csv')
                print("you can check the 'inventory.csv' file.")

            elif m == "T":
                inventory.save_stock('inventory.txt')
                print("you can check the 'inventory.txt'")

            adminMenu(admin)

        elif d == 4:
            print(inventory.stock)
            t = input("Enter the item title:\n")
            i = int(input("Enter the item ID:\n"))
            q = int(input("Enter the quantity:\n"))
            p = float(input("Enter the price:\n"))
            pic = int(input("Enter the lego pieces:\n"))
            age = input("Enter the ege rate:\n")
            it = int(input("Enter the item:\n"))

            new_item = Lego(t,p,pic,age,it,q,i) #ساخت آبجکت لگو و اضافه کردن به انبار
            stuff.append(new_item)
            inventory.add_item(i, q)
            print(inventory.stock)
            adminMenu(admin)


    elif x == 'logout' or x == 'Logout' or x == 'log out' or x == 'Log out':
        print("You're logged out.")
        login()

    else:
        print("Enter a valid command please. ")
        adminMenu(admin)


def mainMenu(username):
    print("Type 'shop' to check Legos.")
    print("Type 'bag' if you want to check your shopping bag.")
    print("Type log out to log out.")
    print("Enter 0 to exit.")
    x = input()

    if x == 'shop' or x == 'Shop' or x == 'SHOP':
        shop(username)

    elif x == 'bag' or x == 'Bag' or x == 'BAG':
        if len(shopping_bag[username]) >= 1:
            for i in shopping_bag[username]:
                print(shopping_bag[username][0].title,shopping_bag[username][0].idCode)
                print(shopping_bag[username][0].price,"$")
                print("")
                x = input(("Type 'checkout' for checking out."))
                if x == 'checkout':
                    buying(shopping_bag[username][0], username)
                else:
                    mainMenu(username)
        else:
            print("Your bag is empty. Let's shop.")
            shop(username)

    elif x == 'logout' or x == 'Logout' or x == 'log out' or x == 'Log out':
        print("You're logged out.")
        login()

    elif x == "0":
        exit(0)

    else:
        print("Enter a valid command please. :)")
        mainMenu(username)


def creatUserAccount():
    name = input('Enter a username: ')

    if name in Users.keys():
        print("Sorry! you can't use this username. Choose another.")
        creatUserAccount()

    password = input('Enter a password. ')
    Users[name] = password
    shopping_bag[name] = []

    print('Welcome ' + str(name) + '! Now login your new user account.')
    AorU()


def TrueUserLogin(username, password):
    TrueUsername = 0
    TruePassword = 0

    if username in Users.keys():
        TrueUsername = 1
        if Users[username] == password:
            TruePassword = 1
            print('Welcome ' + str(username) + '! You are logged in!')
            mainMenu(username)

    if TrueUsername == 1 and TruePassword == 0:
        return 10

# اکانت وجود داره ولی پسورد غلطه
    if TrueUsername == 0 and TruePassword == 0:
        return 11
# اکانت وجود نداره


def TrueAdminLogin(username, password):
    TrueUsername = 0
    TruePassword = 0

    if username in Admins.keys():
        TrueUsername = 1
        if Admins[username] == password:
            TruePassword = 1
            print('Welcom Sir! You are logged in.')
            adminMenu(username)

    if TrueUsername == 1 and TruePassword == 0:
        return 10

# اکانت وجود داره ولی پسورد غلطه
    if TrueUsername == 0 and TruePassword == 0:
        return 11
# اکانت وجود نداره


def AorU():
    x = input('Are you an Admin or a User? Type "A" for admin and "U" for user. ')
    if x == 'A':
        username = input("Enter your user name: ")
        password = input("Enter your password: ")
        t = TrueAdminLogin(username, password)

        if t == 10:
            print("Wrong Password! Try again or create a new account.")
            return 10

        if t == 11:
            print("We can't find your account. Try for another account (user one maybe!) or make one.")
            return 11

    elif x == 'U':
        username = input("Enter your user name: ")
        password = input("Enter your password: ")
        t = TrueUserLogin(username, password)

        if t == 10:
            print("Wrong Password! Try again or create a new account.")
            return 10

        if t == 11:
            print("We can't find your account. Try for another account or make one.")
            return 11

    else:
        print('Enter a valid answer please.(A or U)')
        AorU()


def login():
    x = input("Do you have an account? ")

    if x == 'yes' or x == 'Yes' or x == 'YES':
        i = AorU()
        if i == 10 or i == 11:
            login()

    elif x == 'No' or x == 'NO' or x == 'no':
        print("Let's make one!")
        creatUserAccount()

    else:
        print('Answer with yes/no.')
        login()

