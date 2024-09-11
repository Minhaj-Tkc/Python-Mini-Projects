import random
import string

def generate_password(length):
    # Define character set (letters, digits, and special characters)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Set the length of the password
password_length = int(input("Enter the password length: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Your generated password is: {generated_password}")
