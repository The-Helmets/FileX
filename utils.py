import zipfile
import math

from cryptography.fernet import Fernet
from zipfile import ZipFile
from PIL import Image as Image_tool

class Encryptor():
    def key_gen(self):
        key = Fernet.generate_key()
        return key

    def key_save(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_open(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):

        fer = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = fer.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        fer = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = fer.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)

class Archiever:
    def do_zip(self, zip_name):
        zippy = ZipFile(zip_name, 'w')
        file_path = str(input("Enter the address of the file"))
        zippy.write(file_path)
        zippy.close()
        print("ZIP has be successfully created")

    def do_unzip(self, zip_name):
        if zipfile.is_zipfile(zip_name) is True:
            with ZipFile(zip_name, 'r') as unzipper:
                unzipper.extractall()
            return True
        else:
            print("Not a valid zip file, Please check again!")

class Image:
    def img_resize(self, path, scale):
        image = Image_tool.open(path)
        x, y = image.size
        x2, y2 = math.floor(x-scale), math.floor(y-scale)
        image = image.resize((x2, y2), Image_tool.ANTIALIAS)
        image.save(path, quality = 95)
        print("Image has been resized")