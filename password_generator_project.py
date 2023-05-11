import random
import string

def generate_password(length):
    # Define all possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters at random
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Test the function by generating a password of length 10
n=int(input("enter the length of required password:"))
password = generate_password(n)
print(password)
