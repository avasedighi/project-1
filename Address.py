class Address:
    def __init__(self, username, county, city, details, zipcode, delivery_method, delivery_time):
        self.username = username
        self.county = county
        self.city = city
        self.details = details
        self.zipcode = zipcode
        self.delivery_method = delivery_method
        self.delivery_time = delivery_time

    def __str__(self):
        return f"username: {self.username}\ncounty: {self.county}\ncity: {self.city}\ndetails: {self.details}\nzipcode: {self.zipcode}\ndelivery_method: {self.delivery_method}\ndelivery_time: {self.delivery_time}"

class Logistic:
    def __init__(self, z_capacity=3, a_capacity=3):
        self.z_capacity = z_capacity
        self.a_capacity = a_capacity
        self.users = []
        self.users_address = []

    def display_address_menu(self):
        username = input("Please enter your username:\n")
        self.users.append(username)

        county_dict = {1: "Tehran", 2: "Esfahan", 3: "Tabriz"}
        city_dict = {"Tehran": ["Tehran", "Damavand"], "Esfahan": ["Isfahan", "Kashan"], "Tabriz": ["Tabriz", "Sardroud"]}
        #delivery_dict = {1: "Sobh", 2: "Zohr", 3: "Asr"}

        print("Enter the county code:\n1 : Tehran \n2 : Esfahan \n3 : Tabriz")
        county_code = int(input())
        county = county_dict[county_code]

        if county_code == 1:
            print("Enter the city code:\n1 : Tehran \n2 : Damavand")
        elif county_code == 2:
            print("Enter the county code:\n1 : Isfahan \n2 : Kashan")
        else:
            print("Enter the county code:\n1 : Tabriz \n2 : Sardroud")
        city_code = int(input())
        city = city_dict[county][(city_code) - 1]

        details = input("Enter the datails. it is optional:\n")
        zipcode = input("Enter the zipcode. The zipCode should be 10 digits.\n")
        while len(zipcode) != 10:
            print("Error! ZipCode should be 10 digits.\n")
            zipcode = input("ReEnter the zipcode:\n")

        self.address = Address(username, county, city, details, zipcode, None, None)

    def delivery_method(self):
        if self.address.county == "Tehran":
            self.address.delivery_method = "Peyk"
        else:
            self.address.delivery_method = "Post"

    def delivery_time(self):
        delivery_dict = {1: "Sobh", 2: "Zohr", 3: "Asr"}
        if self.z_capacity and self.a_capacity > 0:
            print("You can choose one of these options for your delivery:\n1: Sobh\n2: Zohr\n3: Asr")
            d_time = int(input("Enter the number:\n"))
            self.address.delivery_time = delivery_dict[d_time]
            if d_time == 2:
                self.z_capacity -= 1
            elif d_time == 3:
                self.a_capacity -= 1
        elif self.z_capacity > 0:
            print("You can choose one of these options for your delivery:\n1: Sobh\n2: Zohr")
            d_time = int(input("Enter the number:\n"))
            self.address.delivery_time = delivery_dict[d_time]
            if d_time == 2:
                self.z_capacity -= 1
        elif self.a_capacity > 0:
            print("You can choose one of these options for your delivery:\n1: Sobh\n3: Asr")
            d_time = int(input("Enter the number:\n"))
            self.address.delivery_time = delivery_dict[d_time]

        else:
            print("You can choose one of these options for your delivery:\n1: Sobh")
            d_time = int(input("Enter the number:\n"))
            self.address.delivery_time = delivery_dict[d_time]

    def confirmation(self):
        print("do you confirm this data? Enter 'Y' if yes. Else enter 'N'.")
        print(self.address)
        con = input()
        if con == "Y":
            print(self.address)
            self.users_address.append(self.address)
            return True
        else:
            return False

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

    #If the user confirms the entered details, print the address
    if confirmed:
        print("Address confirmed.")
    else:
        print("Address not confirmed. Please try again.")

    Frequest = input("do you have any other request? Enter 'Y' if yes. Else enter 'N'.\n\n")
    if Frequest == 'N':
        #for i in logistic.users_address:
         #   print(i,"\n**********")
        exit(0)
