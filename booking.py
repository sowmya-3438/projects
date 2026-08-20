from database import buses, bookings
from email_service import send_booking_email, send_cancellation_email

def find_bus(bus_id):

    for bus in buses:

        if bus["bus_id"] == bus_id:
            return bus

    return None


def book_ticket():

    print("\n")
    print("BOOK TICKET")
    

    try:
        bus_id = int(input("Enter Bus ID: "))

    except ValueError:
        print("Please enter a valid Bus ID.")
        return

    bus = find_bus(bus_id)

    if bus is None:
        print("Bus not found.")
        return

    if bus["available_seats"] == 0:
        print("No seats available.")
        return

    print("\nBus Name    :", bus["bus_name"])
    print("Source      :", bus["source"])
    print("Destination :", bus["destination"])
    print("Date        :", bus["date"])
    print("Time        :", bus["time"])
    print("Fare        :", bus["fare"])
    print("Available   :", bus["available_seats"])

    

    name = input("Enter passenger name: ").strip()
    phone = input("Enter mobile number: ").strip()
    email = input("Enter email address: ").strip()
    gender = input("Enter gender (Male/Female/Other): ").strip()
    try:
        age = int(input("Enter passenger age: "))
        seat_no = int(input("Enter seat number: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    if seat_no < 1 or seat_no > bus["total_seats"]:
        print("Invalid seat number.")
        return

    # Check whether seat is already booked

    for booking in bookings:

        if (
            booking["bus_id"] == bus_id
            and
            booking["seat_no"] == seat_no
            and
            booking["status"] == "Confirmed"
        ):

            print("Seat already booked.")
            return

    ticket_id =  len(bookings) + 1

    booking = {
        "ticket_id": ticket_id,
        "bus_id": bus_id,
        "passenger_name": name,
        "phone": phone,
        "email": email,
        "gender": gender,
        "age": age,
        "seat_no": seat_no,
        
        "bus_name": bus["bus_name"],
        "source": bus["source"],
        "destination": bus["destination"],
        "date": bus["date"],
        "time": bus["time"],
        "fare": bus["fare"],
        "status": "Confirmed"
    }

    bookings.append(booking)

    bus["available_seats"] -= 1

    send_booking_email(
        email,
        booking
    )

    print("\n") 
    print("TICKET BOOKED")
    

    print("Ticket ID      :", ticket_id)
    print("Passenger Name :", name)
    print("Phone          :", phone)
    print("Gender         :", gender)
    print("Age            :", age)
    print("Bus Name       :", bus["bus_name"])
    print("Source         :", bus["source"])
    print("Destination    :", bus["destination"])
    print("Date           :", bus["date"])
    print("Time           :", bus["time"])
    print("Seat Number    :", seat_no)
    print("Fare           :", bus["fare"])
    print("Status         : Confirmed")

    


def cancel_ticket():

    print("\n")
    print("CANCEL TICKET")

    if len(bookings) == 0:
        print("No bookings available.")
        return

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Please enter a valid Ticket ID.")
        return

    for booking in bookings:

        if booking["ticket_id"] == ticket_id:

            if booking["status"] == "Cancelled":
                print("Ticket is already cancelled.")
                return

            booking["status"] = "Cancelled"

            bus = find_bus(booking["bus_id"])

            if bus:
                bus["available_seats"] += 1
            send_cancellation_email(
                booking["email"],
                booking
            )


            print("\nTicket cancelled successfully.")
            print("Ticket ID :", ticket_id)
            print("Status    : Cancelled")

            return

    print("\nTicket not found.")
    
def ticket_history():

    print("\n")
    print(" TICKET HISTORY")
    

    if len(bookings) == 0:
        print("No bookings found.")
        return

    for booking in bookings:

        bus = find_bus(booking["bus_id"])

        print("\nTicket ID      :", booking["ticket_id"])
        print("Passenger Name :", booking["passenger_name"])
        print("Phone          :", booking["phone"])
        print("Gender         :", booking["gender"])
        print("Age            :", booking["age"])
        print("Bus Name       :", bus["bus_name"])
        print("Source         :", bus["source"])
        print("Destination    :", bus["destination"])
        print("Date           :", bus["date"])
        print("Time           :", bus["time"])
        print("Seat Number    :", booking["seat_no"])
        print("Fare           :", bus["fare"])
        print("Status         :", booking["status"])

        