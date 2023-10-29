def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode():
    to_encode = (input("Please enter your password to encode: "))
    encoded = [int(number) + 3 for number in to_encode]
    return encoded

def main():
    while True:
        user_input = input("Please enter an option: ")
        if user_input == "0":
            break
        elif user_input == "1":
            new_password = encode()
            print("Your password has been encoded and stored!")

if __name__ == "__main__":
    main()
