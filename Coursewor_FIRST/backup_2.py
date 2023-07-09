def welcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher. ")

def enter_message():
    valid = ['e','d']
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    
    while mode not in valid:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
    if mode == 'e':
        message = input("What message would you like to encrypt: ")
    else:
        message = input("What message would you like to decrypt: ")
    valid_shift = True
    while valid_shift:
        try:
            shift = int(input("What is the shift number: "))
            valid_shift = False
        except ValueError:
            print("Invalid Shift")
    return mode, message.upper(),shift

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

def is_file(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except FileNotFoundError:
        return False

def write_message(message):
    with open('result.txt','w') as f:
        for i in messages:
            f.write(message + '\n')


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

                

def main():
    welcome()
    while True:
        mode, message, shift = enter_message()
        if mode == 'e':
            encrypted_text = encrypt(message, shift)
            print(encrypted_text)
        else:
            decrypted_text = decrypt(message, shift)
            print(decrypted_text)
        again= ''
        while again.lower() not in ['y', 'n']:
            again = input("Would you like encrypt or decrypt another message? (y/n): ")

        if again.lower() == 'n':
            break
    print("Thanks for using the program, goodbye!")
main()
      
     
        
        
            
    
        
