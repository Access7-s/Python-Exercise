def welcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher. ")

def enter_message():
    if mode == 'e':
        message = input("What message would you like to encrypt: ")
    else:
        message = input("What message would you like to decrypt: ")
    return message.upper()

def encrypt(message, shift):
    encrypted = ''
    for i in message:
        if i.isalpha():
            encrypted += chr((ord(i) - 65 + shift) % 26 + 65)
        else:
            encrypted += i
    return encrypted.upper()

def decrypt(message, shift):
    decrypted = ''
    for i in message:
        if i.isalpha():
            decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        else:
            decrypted += i
    return decrypted.upper()

def process_file(filename,mode):
    message = []
    with open(filename,'r') as f:
        for line in f:
            if mode == 'e':
                data=encrypt(line, shift)
                message.append(data)
            else:
                data=decrypt(line, shift)
                message.append(data)
    return message

def is_file(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except FileNotFoundError:
        return False

def write_message(message):
    with open('results.txt','w') as f:
        for i in messages:
            f.write(message + '\n')

def message_or_file():
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    while mode != 'e' and mode != 'd':
        print("Invalid Mode!")
        mode = input("Would you like to encrypt (e) or decrypt (d): ")

    corf = input('Would you like to read from a file (f) or the console (c)? ')
    while corf != 'f' and corf != 'c':
        print("Invalid Choice!")
        corf = input('Would you like to read from a file (f) or the console (c)? ')

    if corf.lower() == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        message = None
    else:
        filename = None
        message = enter_message()

    return mode, message, filename        

def main():
    welcome()
    while True:
        mode, message, filename = message_or_file()
        while True:
            shift = input("What is the shift number: ")
            if shift.isdigit() and 1 <= int(shift) <= 25:
                shift = int(shift)
                break
            else:
                print("Invalid Shift ")

        if message:
            if mode == 'e':
                result = encrypt(message, shift)
                print(f"Encrypted : {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted : {result}")
        else:
            result = process_file(filename, mode)
            if result:
                write_message(result)
                print("Output written to results.txt")
        while True:
            choice = input("Would you like to encrypt or decrypt another message? (y/n): ")
            if choice == 'y' or choice == 'n':
                break
            else:
                print("Invalid choice! ")
        if choice == 'n':
            break
    

main()
                
    
            
    
        
