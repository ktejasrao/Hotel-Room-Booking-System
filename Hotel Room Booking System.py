import os 
import json
# A Dictionary for all types of rooms
ROOMS={"101":{"Type":"Single","Price":2000},
       "102":{"Type":"Double","Price":3500},
       "201":{"Type":"Suit","Price":6000}}
# Gst rates which will be included while making the final bill
GST_RATE=0.12
FILE_NAME="my_bookings.txt"

current_booking=[]

def load_bookings():
    global current_bookings
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            try:
                current_booking = json.load(file)
            except json.JSONDecodeError:
                current_booking = []
def save_bookings():
    with open(FILE_NAME,'w') as file:
        json.dump(current_booking,file)

# Option No. 1 (View All Bookings)
def view_available():
    booked_rooms = [b["Room"] for b in current_booking]
    print("-----AVAIALABLE ROOMS------")
    available_found =False
    for room_no , details in ROOMS.items():
        if room_no not in booked_rooms:
            print(f"{room_no} {details['Type']} Rs. {details['Price']}")
            available_found = True
    if not available_found:
        print("No rooms are currently available. ")

# Option No. 2 (Book A Room)
def book_room():
    guest_name = input("Guest Name: ")
    room_no = input("Room: ")

    if room_no not in ROOMS:
        print("Invalid room number. ")
        return

    booked_rooms = [b["Room"] for b in current_booking]
    if room_no in booked_rooms:
        print(f"Room {room_no} is already booked. Please choose another room. ")
        return

    try:
        night = int(input("Nights: "))
        if night<1 or night > 30:
            print("Nights must be between 1 an 30.")
            return
    except ValueError:
        print("Invalid input. Nights must be a number. ")

    rate = ROOMS[room_no]["Price"]
    base_cost = rate * night
    gst = base_cost * GST_RATE
    total_bill = base_cost + gst

    booking ={
        "Guest" : guest_name,
        "Room" : room_no,
        "Nights" : night
    }
    current_booking.append(booking)
    save_bookings()

    print(f"\nRoom {room_no} booked for {guest_name} | {night} night(s)")
    print(f"Bill: {base_cost} + GST {int(gst)} = Rs. {int(total_bill)}")

# Option No. 3(Cancel A Booking)
def cancel_booking():
    room_no = input("Enter room number to cancel: ")
    for i, booking in enumerate(current_booking):
        if booking["Room"] == room_no:
            del current_booking[i]
            save_bookings()
            print(f"Booking for room {room_no} cancelled. Room {room_no} is now available.")
            return
    print(f"No active booking found for room {room_no}.")

# A function For Main Menu
def main():
    load_bookings()
    while True:
        print("--- HOTEL ROOM BOOKING SYSTEM ---")
        print("1. View Available Rooms")
        print("2. Book A Room")
        print("3. Cancel A Booking")
        print("4. Exit")

        choice = input("Select An Option: ")

        if choice == "1":
            view_available()
        elif choice == "2":
            book_room()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            print("Exiting System. Goodbyee !")
            break
        else:
            print("Invalid Option. Options Are Upto 4 Only")

if __name__ == "__main__":
    main()

