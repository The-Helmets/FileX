from cryptography.fernet import Fernet
from utils import *

print("\nWelcome to FileX! This is an interactive file management tool.")

enc = Encryptor()
arc = Archiever()
img = Image()

# Main menu
while True:
    user_choice = (int(input("\nWhat would you like to do?\n1. Encrypt or Decrypt\n2. Zip or Unzip \n3. Image Tools \n4. Exit\n\n>>>")))

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
        u_choice = int(input("\nWhat would you like to do?\n1. ZIP\n2. UNZIP\n\n"))
        if u_choice == 1:
            zip_name = str(input("\nPlease enter the name of the zip file to be created: ")) + '.zip'
            arc.do_zip(zip_name)
        
        elif u_choice == 2:
            zip_name = str(input("\nPlease enter the path of the zip file to be unzipped: "))
            arc.do_unzip(zip_name)

    elif user_choice == 3:
        img_path = str(input("\nEnter the image path:\n"))
        img_scale = int(input("\nEnter the scaling amount, 75, 50, 25 : \n\n"))
        img.img_resize(img_path, img_scale)

    elif user_choice == 4:
        print("\nGoodbye!")
        exit()