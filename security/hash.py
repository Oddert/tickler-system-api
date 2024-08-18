'''Hashing functions used by the main authentication logic.'''
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_hashed_pwd(password: str) -> str:
    '''Hashes a raw password first time.'''
    return password_context.hash(password)

def verify_hashed_pwd(password: str, hashed_password: str) -> bool:
    '''Compares a raw password to a stored hashed password.'''
    print('password', password, 'hashed_password', hashed_password)
    return password_context.verify(password, hashed_password)
