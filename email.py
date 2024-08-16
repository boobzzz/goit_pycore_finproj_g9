from typing import TypedDict
from field import Field
import re

class Email(Field):
    def __init__(self, value: str):
        super().__init__(value)
        self.validate_email()

    def validate_email(self):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_regex.fullmatch(self.value):
            self.value = self.value.lower()  
        else:
            self.value = None

class EmailData(TypedDict):
    email: Email
    index: int
