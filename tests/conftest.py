import random
import string
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture()
def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{username}@mail.ru"

@pytest.fixture()
def random_email_not_mask():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{username}@mailru"

@pytest.fixture()
def random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=6))  
    return password
