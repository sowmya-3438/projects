from buses import search_buses
from booking import book_ticket, cancel_ticket, ticket_history
from email.mime.text import MIMEText

def main():

    while True:

        print("\n")
        print("BUS RESERVATION SYSTEM")
    

        print("1. Search Bus")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Ticket History")
        print("5. Exit")

        

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_buses()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            cancel_ticket()

        elif choice == "4":
            ticket_history()

        elif choice == "5":
            print("\nThank you for using Bus Reservation System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()