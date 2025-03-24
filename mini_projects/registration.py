import re
from functools import wraps

class User:
    id = 0

    def __init__(self, username, email, phone, password, password_repeat):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.password_repeat = password_repeat
        self.id = User.id
        User.id += 1
    
    def __repr__(self):
        return f'User({self.username}, {self.email})'
    

def username_validation(fn):
    @wraps(fn)
    def wrapper(user_info, *args, **kwargs):
        reserved_name = ['admin', 'user', 'root', 'superuser']
        if len(user_info['username']) < 5 or len(user_info['username']) > 20:
            raise ValueError('Username must be between 5 and 20 characters')
        if not user_info['username'].isalnum():
            raise ValueError('Username can only contain letters and numbers')
        if user_info['username'].lower() in reserved_name:
            raise ValueError('Username is reserved')
        return fn(user_info, *args, **kwargs)
    return wrapper

def email_validation(fn):
    @wraps(fn)
    def wrapper(user_info, *args, **kwargs):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', user_info['email']):
            raise ValueError('Invalid email address')
        return fn(user_info, *args, **kwargs)
    return wrapper

def phone_validation(fn):
    @wraps(fn)
    def wrapper(user_info, *args, **kwargs):
        if not re.match(r'^\+?\d+$', user_info['phone']):
            raise ValueError
        return fn(user_info, *args, **kwargs)
    return wrapper

def password_validation(fn):
    @wraps(fn)
    def wrapper(user_info, *args, **kwargs):
        if len(user_info['password']) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[a-z]', user_info['password']):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[A-Z]', user_info['password']):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[0-9]', user_info['password']):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*]', user_info['password']):
            raise ValueError('Password must contain at least one special character')
    
        if user_info['password'] != user_info['password_repeat']:
            raise ValueError('Passwords do not match')

        return fn(user_info, *args, **kwargs)
    return wrapper

@password_validation
@phone_validation
@email_validation
@username_validation
def validate(user_data, user_db):
    user = User(user_data['username'], user_data['email'], user_data['phone'], user_data['password'], user_data['password_repeat'])
    user_db[user.id] = user


def user_registration(username, email, phone, password, password_repeat, user_db):
    user_data = {
        'username': username,
        'email': email,
        'phone': phone,
        'password': password,
        'password_repeat': password_repeat
    }
    validate(user_data, user_db)

user_db = {}
user_registration('Alice', 'alice.@gmail.ru', '+37493578612', 'Alice2025*', 'Alice2025*', user_db)
print(user_db)