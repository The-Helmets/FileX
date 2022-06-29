from cryptography.fernet import Fernet

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