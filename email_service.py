import smtplib
import os

from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSKEY = os.getenv("SENDER_PASSKEY")


def send_booking_email(to_email, booking):

    if not SENDER_EMAIL or not SENDER_PASSKEY:
        print("\nEmail configuration is missing.")
        print("Please check your .env file.")
        return False

    subject = "Bus Ticket Booking Confirmation"

    body = f"""
Hello {booking['passenger_name']},

Your bus ticket has been successfully confirmed.


       BUS TICKET CONFIRMATION


ticket ID        : {booking['ticket_id']}
Passenger Name   : {booking['passenger_name']}
Email            : {booking['email']}
Phone Number     : {booking['phone']}
Gender           : {booking['gender']}
Age              : {booking['age']}

BUS DETAILS


Bus Name         : {booking['bus_name']}
Source           : {booking['source']}
Destination      : {booking['destination']}
Date             : {booking['date']}
Time             : {booking['time']}
Seat Number      : {booking['seat_no']}

Fare             : Rs.{booking['fare']}
Status           : {booking['status']}


Thank you for booking with us.

Have a safe journey!

Bus Reservation System
"""

    try:

        message = MIMEMultipart()

        message["From"] = SENDER_EMAIL
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )

        print("\nConnecting to Gmail SMTP server...")

        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        ) as server:

            server.starttls()

            print("Logging into Gmail...")

            server.login(
                SENDER_EMAIL,
                SENDER_PASSKEY
            )

            print("Login successful.")

            server.sendmail(
                SENDER_EMAIL,
                to_email,
                message.as_string()
            )

        print("Email sent successfully!")
        print("Confirmation sent to:", to_email)

        return True

    except smtplib.SMTPAuthenticationError:

        print("\nEmail authentication failed.")
        print("Check your Gmail address and App Password.")

        return False

    except Exception as error:

        print("\nEmail sending failed.")
        print("Error:", error)

        return False
def send_cancellation_email(to_email, booking):

    if not SENDER_EMAIL or not SENDER_PASSKEY:
        print("\nEmail configuration is missing.")
        return False

    subject = "Bus Ticket Cancellation Confirmation"

    body = f"""
Hello {booking['passenger_name']},

Your bus ticket has been successfully cancelled.


       BUS TICKET CANCELLATION


Ticket ID        : {booking['ticket_id']}
Passenger Name   : {booking['passenger_name']}
Email            : {booking['email']}
Phone Number     : {booking['phone']}
Gender           : {booking['gender']}
Age              : {booking['age']}

BUS DETAILS


Bus Name         : {booking['bus_name']}
Source           : {booking['source']}
Destination      : {booking['destination']}
Date             : {booking['date']}
Time             : {booking['time']}
Seat Number      : {booking['seat_no']}

Fare             : Rs.{booking['fare']}
Status           : {booking['status']}



Your ticket has been cancelled successfully.

Thank you for using our Bus Reservation System.
"""

    try:

        message = MIMEMultipart()

        message["From"] = SENDER_EMAIL
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(
                SENDER_EMAIL,
                SENDER_PASSKEY
            )

            server.sendmail(
                SENDER_EMAIL,
                to_email,
                message.as_string()
            )

        print("Cancellation email sent successfully!")
        print("Confirmation sent to:", to_email)

        return True

    except smtplib.SMTPAuthenticationError:

        print("\nEmail authentication failed.")
        print("Check your Gmail App Password.")

        return False

    except Exception as error:

        print("\nEmail sending failed.")
        print("Error:", error)

        return False