# Consist generators

import string
import random
from typing import List


def password_gen():
    """
    Generates password which consist letters big, small and digits
    """

    while True:
        p = "".join(random.choices(string.ascii_letters + string.digits, k=16))
        yield p

def login_gen():
    """ 
    Generates login which consist lower letters and numbers
    """

    while True:
        l = "".join(
            random.choices(
                string.ascii_letters.lower() + string.digits, k=random.randint(3, 16)
            )
        )
        yield l

def custom_number_gen(gen_range: List[int]):
    """
    Generates custom number within given range
    """

    while True:
        num = random.randint(gen_range[0], gen_range[1])
        yield num

def custom_string_gen(big_letters: bool, digits: bool, gen_range: List[int]):
    """ 
    Generates custom text
    """

    while True:
        l = "".join(
            random.choices(
                (
                    (
                        string.ascii_letters.lower()
                        if not big_letters
                        else string.ascii_letters
                    )
                    + string.digits
                    if digits
                    else string.ascii_letters
                ),
                k=random.randint(gen_range[0], gen_range[1]),
            )
        )
        yield l

def country_gen():
    """
    Generates country code
    """

    country_codes = [".pl", ".de", ".fr", "co.uk", ".us"]
    # choice = "".join(random.choices(country_codes, k=1))
    choice = country_codes[random.randint(0, len(country_codes) - 1)]
    yield choice

def domain_gen():
    """
    Generates domain name
    """

    while True:
        d = "".join(
            random.choices(
                string.ascii_letters.lower() + string.digits, k=random.randint(2, 4)
            )
        )
        yield d

def email_gen():
    """
    Generates email
    """

    while True:
        email = "".join(
            login_gen().__next__()
            + "@"
            + domain_gen().__next__()
            + country_gen().__next__()
        )
        yield email

def user_payload_gen():
    """
    Generates user payload
    """

    while True:
        user_payload = {
            "email": email_gen().__next__(),
            "password": password_gen().__next__()
        }
        yield user_payload
