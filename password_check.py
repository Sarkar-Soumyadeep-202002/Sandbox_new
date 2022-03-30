"""
Name: Soumyadeep Sarkar
Description: Password checker

"""


def is_valid(password, length):
    if len(password) < length:
        return False
    else:
        return True


def main():
    password = input("Enter your password: ")
    length = 10
    print(f"Your password is valid? {is_valid(password,length)}")
    for char in range(0, len(password)):
        print('*', end='')


main()
