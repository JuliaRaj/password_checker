#writing a python program to check the validity of a password
#A VALID PASSWORD MUST HAVE:
#1. At least 8 characters
#2. At least one uppercase letter
#3. At least one lowercase letter
#4. At least one digit
#5. At least one special character (e.g., @, #, $, etc.)

def is_valid_password(password):
    #checking the length of the password (should be atleast 8 characters)
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Flags for each requirement:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()_+-=[]\\{}|;':"

    #checking each character in the passwordth
    for char in password:
        if char.isupper():
            has_upper = True
            #checking if the character is uppercase
        elif char.islower():
            has_lower = True
            #checking if the character is lowercase
        elif char.isdigit():
            has_digit = True
            #checking if the character is a digit
        elif char in special_characters:
            has_special = True
            #checking if the character is a special character

    #checking if all the conditions are met
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character."
    
    return "Password is valid."
#user input for the password
password = input("Enter password")

#validate password
print(is_valid_password(password))
# This script checks the validity of a password based on specific criteria.
# It checks for length, presence of uppercase letters, lowercase letters, digits, and special characters.
# If the password meets all criteria, it returns "Password is valid."
# If it fails any criteria, it returns a specific error message.