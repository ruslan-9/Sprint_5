import random
import string

def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{username}@mail.ru"

def random_email_not_mask():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{username}@mailru"

def random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=6))  
    return password
