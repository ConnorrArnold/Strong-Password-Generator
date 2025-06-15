import random
import string

def generate_password(length=12):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = uppercase + lowercase + digits
    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining_length)

    random.shuffle(password_chars)

    return ''.join(password_chars)

print("New Password:", generate_password())