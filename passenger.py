import re


def get_passenger_details():

    
    print("PASSENGER DETAILS")
    

    name = input("Passenger Name : ").strip()

    while True:

        email = input("Email : ").strip()

        if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            break

        print("Invalid email. Please enter a valid email.")

    while True:

        phone = input("Phone Number : ").strip()

        if phone.isdigit() and len(phone) == 10:
            break

        print("Phone number must contain exactly 10 digits.")

    age = input("Age : ").strip()

    gender = input("Gender : ").strip()

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "age": age,
        "gender": gender
    }