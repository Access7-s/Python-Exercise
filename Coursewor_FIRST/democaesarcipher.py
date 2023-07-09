import os

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.\n")

def enter_message():
    while True:
        mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")
        if mode.lower() not in ['e', 'd']:
            print("Invalid mode selected. Please try again.")
        else:
            break
    
    message = input("Enter the message you would like to encrypt or decrypt: ").upper()
    return mode.lower(), message

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    decrypted = ""
    for char in message:
        if char.isalpha():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted += char
    return decrypted

def process_file(filename, mode):
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if mode == 'e':
                messages.append(encrypt(line, 3))
            else:
                messages.append(decrypt(line, 3))
    return messages

def is_file(filename):
    return os.path.isfile(filename)

def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    while True:
        mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")
        if mode.lower() not in ['e', 'd']:
            print("Invalid mode selected. Please try again.")
            continue
        break

    while True:
        input_type = input("Enter 'f' to process a file or 'm' to process a message: ")
        if input_type.lower() not in ['f', 'm']:
            print("Invalid input type selected. Please try again.")
            continue
        break
    
    if input_type.lower() == 'f':
        while True:
            filename = input("Enter the filename: ")
            if not is_file(filename):
                print("File does not exist. Please try again.")
                continue
            break
        message = None
    else:
        filename = None
        message = input("Enter the message: ").upper()
    
    return mode.lower(), message, filename


def main():
    welcome()

    while True:
        mode, message, filename = message_or_file()
        
        if filename:
            messages = process_file(filename, mode)
            print("Messages processed from file:")
            for message in messages:
                print(message)
        else:
            if mode == 'e':
                shift = int(input("What is the shift number: "))
                encrypted_message = encrypt(message, shift)
                print("Encrypted message:", encrypted_message)
                write_messages([encrypted_message])
            else:
                shift = int(input("What is the shift number: "))
                decrypted_message = decrypt(message, shift)
                print("Decrypted message:", decrypted_message)
                write_messages([decrypted_message])
        
        while True:
            another = input("Would you like to encrypt/decrypt another message? (y/n): ")
            if another.lower() not in ['y', 'n']:
                print("Invalid input selected. Please try again.")
                continue
            break
        if another.lower() == 'n':
            break

if __name__ == "__main__":
    main()
