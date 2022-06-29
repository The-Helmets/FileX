from cryptography.fernet import Fernet
from utils import *

print("\nWelcome to FileX! This is an interactive file management tool.")

enc = Encryptor()

# Main menu
while True:
    user_choice = (int(input("\nWhat would you like to do?\n1. Encrypt or Decrypt\n2. Zip or Unzip \n3.  Image Tools \n4.  Exit\n\n>>>")))

    if user_choice == 1:
        u_choice = int(input("\nWhat would you like to do?\n1. Encrypt\n2. Decrypt\n\n"))
        if u_choice == 1:
            f_path = str(input("\nPlease enter the address of the file: "))
            e_key = enc.key_gen()
            enc.key_save(e_key, 'my_key.key')
            enc.file_encrypt(e_key, f_path, 'encrypted_file')
            print("Encrypted")
            
        elif u_choice == 2:
            d_key = enc.key_open('my_key.key')
            enc.file_decrypt(d_key, 'en_LICENSE', 'n_LICENSE')
            print("Decrypted")

    elif user_choice == 2:
            print("WIP Archiever")

    elif user_choice == 3:
            print("WIP Image Tools")

    elif user_choice == 4:
        print("\nGoodbye!")
        exit()