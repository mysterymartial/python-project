import string
from unittest import TestCase
from task.password_generator import PasswordGenerator


class TestPassword(TestCase):
    def test_default_length(self):
        generator = PasswordGenerator()
        password = generator.generate_password()
        self.assertEqual(len(password), 16)
    def test_custom_length(self):
        generator = PasswordGenerator(password_length=12)
        password = generator.generate_password()
        self.assertEqual(len(password), 12)
    def test_Only_upper_Case(self):
        generator = PasswordGenerator(lowercase=False, uppercase=True,white_space=False,numbers=False,special_chars=False)
        password = generator.generate_password()
        self.assertTrue(password.isupper())

    def test_Only_lower_Case(self):
        generator = PasswordGenerator(uppercase=False,numbers=False,special_chars=False,white_space=False,)
        password = generator.generate_password()
        self.assertTrue(password.islower())

    def test_Only_Numbers(self):
        generator = PasswordGenerator(numbers=True,special_chars=False,white_space=False,uppercase=False,lowercase=False)
        password = generator.generate_password()
        self.assertTrue(password.isnumeric())
        self.assertFalse(password.isspace())

    def test_Only_special_chars(self):
        generator = PasswordGenerator(special_chars=True,white_space=False,uppercase=False,lowercase=False,numbers=False)
        password = generator.generate_password()
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_Only_for_white_space(self):
        generator = PasswordGenerator(white_space=True)
        password = generator.generate_password()
        self.assertTrue(password.isspace())
    def test_combined_password(self):
        generator = PasswordGenerator(lowercase=True,numbers=True,special_chars=True,white_space=True,password_length=20,uppercase=True)
        password = generator.generate_password()
        self.assertTrue(any(char in password for char in string.punctuation for char in password))
        self.assertTrue(any(char in password for char in string.digits for char in password))
        self.assertTrue(any(char in password for char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in password for char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in password for char in string.whitespace for char in password))
        self.assertEqual(len(password), 20)


