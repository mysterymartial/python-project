import random
import string

class PasswordGenerator:
    def __init__(cls, password_length=16, uppercase=True, lowercase=True, numbers=True, special_chars=True,white_space =True):
        cls.password_length = password_length
        cls.uppercase = uppercase
        cls.lowercase = lowercase
        cls.numbers = numbers
        cls.special_chars = special_chars
        cls.white_space = white_space
    def generate_password(cls):
            character = ""
            if cls.uppercase:
                character = string.ascii_uppercase
            if cls.lowercase:
                character = string.ascii_lowercase
            if cls.numbers:
                character = string.digits
            if cls.special_chars:
                character = string.punctuation
            if cls.white_space:
                character = string.whitespace
            password = ''.join(random.choice(character)for count in range(cls.password_length))
            return password

