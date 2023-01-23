from Rooms import Rooms
from customers1 import Customers
from BookingAi import Booking

# from  import Booking

def main():
    # filedata = Rooms.load_rooms("./data/Rooms.json")
    # customers = Customers.load_customers_from_file("customers.json")
    # bookings = Customers.load_bookings_from_file("bookings.json")
    while True:
        print("1. Add a new room")
        print("2. Add a new customer")
        print("3. Book a room")
        print("4. Cancel booking")
        print("5. Display all rooms")
        print("6. Display all customers")
        print("7. Display all bookings")
        print("8. Display booked rooms for a specific date")
        print("9. Display available rooms for a specific date")
        print("10. Find room by type")
        print("11. Find room by number")
        print("12. Find customer by name")
        print("13. Remove room")
        print("14. Remove customer")
        print("15. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            choice1 = input("Enter room type \n1 for Basic\n2 for Deluxe\n3 for Suite:\n ")
            if choice1 == "1":
                room_type = "Basic"
                size = "22mr"
                capacity = 10
                number_of_beds = 2
                price = 100
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
            elif choice1 == "2":
                size = "26mr"
                capacity = 10
                number_of_beds = 2
                room_type = "Deluxe"
                price = 200
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
            elif choice1 == "3":
                size = "30mr"
                capacity = 10
                number_of_beds = 4
                room_type = "Suite"
                price = 300
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            customer_city = input("Enter customer city: ")
            customer_email = input("Enter customer email: ")
            customer_age = input("Enter customer age: ")

            Cust = Customers(customer_name, customer_address, customer_city, customer_email, customer_age)
            Cust.add_data()
            print("Customer added.")
        elif choice == "3":
            customer_id = int(input("Enter customer id: "))
            room_id = int(input("Enter room id: "))
            arrival_date = str(input("Enter arrival date (YYYY-MM-DD): "))
            departure_date = str(input("Enter departure date (YYYY-MM-DD): "))
            Book=Booking(customer_id,room_id,arrival_date,departure_date)
            Book.add_booking()



            # Book=Booking(bookings, customer_id, room_id, arrival_date, departure_date, total_price)

        elif choice == "4":
            customer_id = int(input("Enter customer id: "))
            #booking=Booking()
            Booking.cancel_booking(customer_id)
            #booking_id = input("Enter booking id: ")
            #Bookings
            pass

        elif choice == "5":
            Room=Rooms.display_All_Rooms()
            for R in Room:
                ID = R[0]
                Size = R[1]
                Capacity = R[2]
                NumberOfBeds = R[3]
                Type = R[4]
                Price = R[5]
                print(f"Room Number: {ID}")
                print(f"Size Of The Room is: {Size}")
                print(f"Room type: {Type}")
                print(f"Capacity: {Capacity}")
                print(f"NumberOfBeds: {NumberOfBeds}")
                print(f"Price: {Price}\n\n\n")
                print("")
        elif choice == "6":
            Cust=Customers.display_All_Customers()
            for R in Cust:
                name = R[0]
                Address = R[1]
                City = R[2]
                Email = R[3]
                Age = R[4]
                ID = R[5]
                print(f"Customer ID: {ID}")
                print(f"name Of The Customer is: {name}")
                print(f"Address Of The Customer is: {Address}")
                print(f"City Of The Customer Is: {City}")
                print(f"Email Of The Customer: {Email}")
                print(f"Age Of The Customer: {Age}\n\n\n")
                print("")

        elif choice == "7":
            Book=Booking.view_bookings()
            for R in Book:
                CustID = R[0]
                RoomID = R[1]
                ArrivalDate = R[2]
                DepartureDate = R[3]
                TotalPrice = R[4]
                print(f"Customer ID Is: {CustID}")
                print(f"Room Number Is: {RoomID}")
                print(f"ArrivalDate Is: {ArrivalDate}")
                print(f"DepartureDate Is : {DepartureDate}")
                print(f"TotalPrice Is: {TotalPrice}")
                print("")

            # Booking.display_all_bookings(bookings)
        elif choice == "8":
            date = input("Enter date (YYYY-MM-DD): ")
            Book=Booking.BookedRoomsSpecificDate(date)
            if len(Book)>0:

                for B in Book:
                    name = B[0]
                    Type = B[1]
                    ArrivalDate = B[2]

                    print(f"Customer Name: {name}")
                    print(f"Room Type Is: {Type}")
                    print(f"ArrivalDate is: {ArrivalDate}")
                    print("")
            else:
                print(f"there is no reservetions For Your Date")
        elif choice == "9":
            date = input("Enter date (YYYY-MM-DD): ")
            Book=Booking.AvailableroomsSpecificDate(date)
            if Book != False:
                for B in Book:
                    Number_Of_Room = B

                    print(f"Room {int(Number_Of_Room)} Available in {date}")
                    print("")
            else:
                print(f"there is no Room Available In :{date}")
        # Room.display_available_rooms_for_date(rooms, bookings, date)
        elif choice == "10":
            RoomType=input("Enter Room Type")
            room=Rooms.RoomByType(RoomType)
            if room != False:
                for R in room:
                    ID = R[0]
                    Size = R[1]
                    Capacity = R[2]
                    NumberOfBeds = R[3]
                    Type = R[4]
                    Price = R[5]
                    print(f"Room Number Is: {ID}")
                    print(f"Room Size Is: {Size}")
                    print(f"Room Capacity Is: {Capacity}")
                    print(f"Room NumberOfBeds Is: {NumberOfBeds}")
                    print(f"Room Type Is : {Type}")
                    print(f"Room Price Is: {Price}")
                    print("")

            else:
                print(f"Room Not Exist!")

        elif choice == "11":
            Number=input("Enter The Room Number")
            Room=Rooms.RoomByNumber(Number)
            if Room != False:

                print(f"\nSize: {Room.Size}")

                print(f"Capacity: {Room.Capacity}")

                print(f"NumberOfBeds: {Room.NumberOfBeds}")

                print(f"Type: {Room.Type}")

                print(f"Price: {Room.Price}\n")
            else:
                print(f"\nRoom {Number} Not Exist\n")


        elif choice == "12":
            Name = input("Enter Customer Name")

            Cust=Customers.Cust_by_name(Name)
            if Cust != False:
                for R in Cust:
                    name = R[0]
                    Address = R[1]
                    City = R[2]
                    Email = R[3]
                    Age = R[4]
                    ID = R[5]
                    print(f"Customer ID Is: {ID}")
                    print(f"Customer Name Is: {name}")
                    print(f"Customer Address Is: {Address}")
                    print(f"Customer City Is: {City}")
                    print(f"Customer Email Is : {Email}")
                    print(f"Customer Age Is: {Age}")
                    print("")

            else:
                print(f"Customer Not Exist!")


            # customer_name = input
        elif choice == "13":
            Number = input("Enter The Room Number")
            if Rooms.Remove_Room(int(Number)):
                print("Success", "Room Removed Successfully!")
            else:
                print("Failed", "Room not Exist!")

        elif choice == "14":
            Name = input("Enter Customer Name")
            if Customers.Remove_customer(Name):
                print("Sucess", "Customer Removed Successfully!")
            else:
                print("Failed", "Customer not Exist!")

main()
