from unittest import TestCase
from task.email import validate_email


class TestEmail(TestCase):
    def test_email_validation(self):
        self.assertTrue(validate_email("bolasax@native.Africa"))

        self.assertTrue(validate_email("bolasax16@gmail.com"))

    def test_invalid_email(self):
        with self.assertRaises(ValueError ):
            validate_email("123456.com@145667")
        with self.assertRaises(ValueError):
            validate_email("hyvlvgtcdfr.....gvj./")
