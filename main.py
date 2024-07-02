import random


def generate_password(length):
    characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
def main():
    num_passwords = int(input("Введите количество паролей: "))
    password_length = int(input("Введите длину паролей: "))
    passwords = []
    for i in range(num_passwords):
        passwords.append(generate_password(password_length))
    for password in passwords:
        print(password)
if __name__ == "__main__":
    main()