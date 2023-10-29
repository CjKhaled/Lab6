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

def decoder(encoded_string):
    encoded_list = list(encoded_string)

    for i in range(0, len(encoded_list)):
        encoded_list[i] = int(encoded_list[i])
        encoded_list[i] -= 3
        if encoded_list[i]<0:
            encoded_list[i] += 10
        encoded_list[i] = str(encoded_list[i])

    return ''.join(encoded_list)
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
