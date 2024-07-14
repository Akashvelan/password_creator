import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get the desired length of the password from the user
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if _name_ == "_main_":
    main()
