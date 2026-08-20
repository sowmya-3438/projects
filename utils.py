import random
import string


def generate_booking_id():
    letters = ''.join(
        random.choices(string.ascii_uppercase, k=3)
    )

    numbers = ''.join(
        random.choices(string.digits, k=6)
    )

    return letters + numbers


def generate_pnr():
    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=10
        )
    )