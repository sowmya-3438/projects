from database import buses


def search_buses():

    source = input("Enter source: ").strip()
    destination = input("Enter destination: ").strip()
    date = input("Enter date (DD-MM-YYYY): ").strip()

    found = False

    print("\n")
    print("AVAILABLE BUSES")
    

    for bus in buses:

        if (
            bus["source"].lower() == source.lower()
            and
            bus["destination"].lower() == destination.lower()
            and
            bus["date"] == date
        ):

            found = True

            print("Bus ID          :", bus["bus_id"])
            print("Bus Name        :", bus["bus_name"])
            print("Source          :", bus["source"])
            print("Destination     :", bus["destination"])
            print("Date            :", bus["date"])
            print("Time            :", bus["time"])
            print("Available Seats :", bus["available_seats"])
            print("Fare            :", bus["fare"])

        

    if not found:
        print("\nNo buses found.")