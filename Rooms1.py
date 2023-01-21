filename = "./data/Customers.json"




class Room:
    def __init__(self, Type, Size, Capacity, NumberOfBeds, Price):
        self.Type = Type
        self.Size = Size
        self.Capacity = Capacity
        self.NumberOfBeds = NumberOfBeds
        self.Price = Price

    def interduction(self):
        Choose=input(f"""Hello, You chose the {self.Type} Room. Do You Want To Cuntinue?
1.Yes
2.No""")
        with open("Rooms.txt","r+") as f:
            if self.Type=="Basic":
                f.read()
                f.basic

        #if Choose==1:


    # def Room1(self):
    #     data = {}
    #     with open(filename, 'r', encoding='utf-8') as f:
    #         temp = json.load(f)
    #
    #     temp.append(data)
    #     with open(filename, "w") as f:
    #         json.dump(temp, f, indent=4)

    # def type(self):
    #     if self.Type == "Basic":
    #         return ("Hi\nWelcome To Almog Hotel\nYou Choose The Basic Room")
    #
    #     elif self.Type == "Deluxe":
    #         return ("Hi\nWelcome To Almog Hotel\nYou Choose The Deluxe Room")
    #     elif self.Type == "Suite":
    #         return ("Hi\nWelcome To Almog Hotel\nYou Choose The Suite Room")
    #     else:
    #         raise Exception(
    #             "sorry we Dont have this Room\n We Have 3 Types Of Rooms Please Try Again With This Room Types:\n1.Basic\n2.Deluxe\n3.Suite ")

    # def capacity(self):
    #     if self.Type == "Basic":
    #         self.capacity = 100
    #         print(self.City)
    #         return (self.capacity)
    #     elif self.Type == "Deluxe":
    #         self.capacity = 8
    #         return (self.capacity)
    #     elif self.Type == "Suite":
    #         self.capacity = 8
    #         return (self.capacity)
    #         # with open("Suite.txt", "w+") as f:
    #         #     f.read()
    #
    #     else:
    #         raise Exception("sorry we Dont have this Room")
    #
    # def size(self):
    #     if self.Type == "Basic":
    #         self.size = "22Mr"
    #         return (self.size)
    #     elif self.Type == "Deluxe":
    #         self.size = "24Mr"
    #         return (self.size)
    #     elif self.Type == "Suite":
    #         self.size = "24Mr"
    #         return (self.size)
    #     else:
    #         raise Exception("sorry we Dont have this Room")
    #
    # def beds(self):
    #     if self.Type == "Basic":
    #         self.NumberOfBeds = 2
    #         return (self.NumberOfBeds)
    #     elif self.Type == "Deluxe":
    #         self.NumberOfBeds = 3
    #         return (self.NumberOfBeds)
    #     elif self.Type == "Suite":
    #         self.NumberOfBeds = 4
    #         return (self.NumberOfBeds)
    #
    # def price(self):
    #     if self.Type == "Basic":
    #         self.price = "100$"
    #         return (self.price)
    #     elif self.Type == "Deluxe":
    #         self.price = "300$"
    #         return (self.price)
    #     elif self.Type == "Suite":
    #         self.price = "600$"
    #         return (self.price)

    # def id(self):
    #     if self.Type == "Basic" and self.id <= 100:
    #         self.id += 1
    #     elif self.Type == "Deluxe" and self.id <= 80:
    #         self.id += 1
    #     elif self.Type == "Suite" and self.id <= 40:
    #         self.id += 1
    #     else:
    #         raise Exception("sorry we Dont have this Room")
    def __str__(self):
        return (f"""You Choose Out {self.Type} Room
The Room Price Is:{self.price} for 1 Night
The Room Size Is:{self.size} 
The Room Has {self.beds} Beds
Do You Want To Continue To Reservation?
1.Yes 
2.No     
""")

# class Customers
#     def __init__(self,Id,Name,Address,City,Email,Age):
#         pass
# class Bookings:
#     def __init__(self,CustID,RoomID,ArrivalDate,DepartureDate,TotalPrice):
#         pass
# room = rooms("Deluxe")
# print(room.Room())
# print(room.capacity())
# print(room.size())
# print(room.numerofbeds())
