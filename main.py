
# Password Policy Validation Engine

# Password policy settings
MIN_LENGTH = 8

PROHIBITED_WORDS = [
    "password",
    "admin",
    "qwerty",
    "1234"
]


# Function to check minimum length
def check_length(password):
    if len(password) < MIN_LENGTH:
        return False
    return True


# Function to check uppercase letter
def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


# Function to check lowercase letter
def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


# Function to check digit
def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


# Function to check special character
def check_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False


# Function to check consecutive repeated characters
def check_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False
    return True


# Function to check prohibited substrings
def check_prohibited(password):
    lower_password = password.lower()

    for word in PROHIBITED_WORDS:
        if word in lower_password:
            return False
    return True


# Function to validate password
def validate_password(password):

    failed_conditions = []

    if not check_length(password):
        failed_conditions.append(
            "Password must contain at least 8 characters."
        )

    if not check_uppercase(password):
        failed_conditions.append(
            "Password must contain at least one uppercase letter."
        )

    if not check_lowercase(password):
        failed_conditions.append(
            "Password must contain at least one lowercase letter."
        )

    if not check_digit(password):
        failed_conditions.append(
            "Password must contain at least one digit."
        )

    if not check_special(password):
        failed_conditions.append(
            "Password must contain at least one special character."
        )

    if not check_repetition(password):
        failed_conditions.append(
            "Password must not contain three consecutive identical characters."
        )

    if not check_prohibited(password):
        failed_conditions.append(
            "Password contains a prohibited word or sequence."
        )

    return failed_conditions


# Main program
print("==========================================")
print("      PASSWORD POLICY VALIDATION")
print("==========================================")

print("\nPassword Rules:")
print("1. Minimum 8 characters")
print("2. At least one uppercase letter")
print("3. At least one lowercase letter")
print("4. At least one digit")
print("5. At least one special character")
print("6. No three consecutive identical characters")
print("7. No prohibited words or sequences")

n = int(input("\nEnter number of passwords to check: "))

if n <= 0:
    print("Please enter a valid number of passwords.")

else:

    for i in range(n):

        print("\n------------------------------------------")
        print("Password", i + 1)

        password = input("Enter sample password: ")

        errors = validate_password(password)

        if len(errors) == 0:

            print("Result: VALID PASSWORD")
            print("All password rules are satisfied.")

        else:

            print("Result: INVALID PASSWORD")
            print("Failed Conditions:")

            for error in errors:
                print("-", error)

        print("------------------------------------------")

print("\nPassword validation completed.")
