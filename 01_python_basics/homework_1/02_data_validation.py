def data_validation():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    name_valid = validate_name(name)
    age_valid = validate_age(age)
    email_valid = validate_email(email)
    password_valid = validate_password(password)

    if all([name_valid, age_valid, email_valid, password_valid]):
        print("All data is valid")
    else:
        print("Data validation failed")


def validate_name(name: str):
    valid = True
    if len(name) < 5:
        print("Name must contain at least 5 characters")
        valid = False
    if name and name[0].isdigit():
        print("Name cannot start with a digit")
        valid = False
    if any(char.isspace() for char in name):
        print("Name cannot contain spaces")
        valid = False
    return valid


def validate_email(email: str):
    if email.count("@") != 1:
        print("Email must contain exactly one @")
        return False
    return True


def validate_age(user_age: str) -> bool:
    valid = True
    if not user_age.isdigit():
        print("Age must contain digits only")
        valid = False
    elif int(user_age) < 16:
        print("Age must be at least 16")
        valid = False
    return valid


def validate_password(password: str):
    valid = True

    if len(password) < 8:
        print("Password must contain at least 8 characters")
        valid = False
    if any(char.isspace() for char in password):
        print("Password cannot contain spaces")
        valid = False
    if len(set(password)) == 1:
        print("Password cannot consist of identical characters")
        valid = False
    return valid


data_validation()
