# Author : Shibin Shaji, Yiwei Li
# Date : 23, January 2025
# Description : Purpose of this program is to create a secure password
import random
import string

# Function to get user input
def get_user_input(prompt, min_value, max_value):
    valid_input = False
    while not valid_input:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                valid_input = True
                return value
            print(f"Enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def generate_password(length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials > length:
        print("The sum of letters, digits, and special characters exceeds the total length.")
        return ""

    # Generate required characters using range
    letters = [random.choice(string.ascii_letters) for _ in range(num_letters)]
    digits = [random.choice(string.digits) for _ in range(num_digits)]
    specials = [random.choice(string.punctuation) for _ in range(num_specials)]

    # Filling remaining characters
    remaining = length - (num_letters + num_digits + num_specials)
    filler = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining)]

    # Shuffling characters
    all_characters = letters + digits + specials + filler
    random.shuffle(all_characters)

    return ''.join(all_characters)

# Menu function
def main():
    print("\n--- Secure Password Generator ---\n")

    # Getting total password length
    total_length = get_user_input("Enter the total length of the password (minimum 8): ", 8, 13)

    # Getting length of each character
    num_letters = get_user_input(f"Enter the number of letters (0 to {total_length}): ", 0, total_length)
    num_digits = get_user_input(f"Enter the number of digits (0 to {total_length}): ", 0, total_length)
    num_specials = get_user_input(f"Enter the number of special characters (0 to {total_length}): ", 0, total_length)

    # Validate the sum of characters
    while num_letters + num_digits + num_specials > total_length:
        print("The sum of letters, digits, and special characters exceeds the total length. Please try again.")
        num_letters = get_user_input(f"Enter the number of letters (0 to {total_length}): ", 0, total_length)
        num_digits = get_user_input(f"Enter the number of digits (0 to {total_length}): ", 0, total_length)
        num_specials = get_user_input(f"Enter the number of special characters (0 to {total_length}): ", 0, total_length)



