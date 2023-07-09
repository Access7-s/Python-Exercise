def welcome():
    '''This function displays Welcome message '''
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher. ")

def enter_message():
    '''Asks user for mode and operation type i.e, via console or file that is taking message from console or file'''
    valid = ['e','d']
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    #checks if the mode is correct and reexecutes the prompt command until it is correct
    while mode not in valid:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d): ")

    corf = input('Would you like to read from a file (f) or the console (c)? ')
    while corf != 'f' and corf != 'c':
        print("Invalid choice")
        corf = input('Would you like to read from a file (f) or the console (c)? ')

    return mode, corf

def encrypt(message, shift):
    '''Encrypts message and returns the encrypted message in uppercase.'''
    encrypted = ''
    for i in message:
        #checks if i is alphabet letters(a-z)
        if i.isalpha():
            encrypted += chr((ord(i) - 65 + shift) % 26 + 65)
        else:
            encrypted += i
    #returns message in uppercase        
    return encrypted.upper()

def decrypt(message, shift):
    '''Encrypts message and returns the encrypted message in uppercase.'''
    decrypted = ''
    for i in message:
        if i.isalpha():
            #chr returns alphabet from ascci unicode and ord returns unicode from character
            decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        else:
            decrypted += i
    #returns uppercase message
    return decrypted.upper()

def process_file(filename,mode,shift):
    '''This function process the file, that is, reads the message(string) one by one and encrypts or decrypts as per mode and appends/ add the vaalue to the empty list '''
    message = []
    #opens file to read stored in f
    #append(data) adds string to "message" (empty list)
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
    '''This function checks if the file is in the working directory '''
    #Using exception handling for FilenotfoundError
    try:
        with open(filename, 'r') as f:
            return True
    except FileNotFoundError:
        return False

def write_message(message):
    '''This file writes the message as per mode in a text file "result.txt" '''
    #writing message in result.txt by opening file in write mode
    with open('results.txt','w') as f:
        for data in message:
            f.write(data + '\n')

def message_or_file():
    '''This function ask user for console or file use, and runs the program as per the choice and returns the mode, message in upper case and the input taking method i.e, console or file'''
    mode, corf = enter_message()
    if corf == 'f':
        message = input("Enter a filename: ")
        valid = is_file(message)
        while not valid:
            print("Invalid Filename")
            message = input("Enter a filename: ")
            valid = is_file(message)
    else:
        if mode == 'e':
            message = input("What message would you like to encrypt: ")
        else:
            message = input("What message would you like to decrypt: ")
    return mode, corf , message.upper()
        

def main():
    '''This function operates and calls the function sequencially as per need and executes the program '''
    #displays welcome message
    welcome()
    while True:
        mode, corf, message = message_or_file()
        while True:
            shift = input("What is the shift number: ")
            if shift.isdigit() and 1 <= int(shift) <= 25:
                shift = int(shift)
                break
            else:
                print("Invalid Shift ")
        if corf == "c":
            if mode == 'e':
                result = encrypt(message, shift)
                print(result)
            else:
                result = decrypt(message, shift)
                print(result)
        else:
            result = process_file(message, mode, shift)
            write_message(result)
            print("Output written to results.txt")
        while True:
            #asks user for reexecution of program
            choice = input("Would you like to encrypt or decrypt another message? (y/n): ")
            if choice == 'y' or choice == 'n':
                break
            else:
                print("Invalid choice! ")
        if choice == 'n':
            break
        #prints goodbye message
    print('Thanks for using the program, goodbye!')
    

main()
