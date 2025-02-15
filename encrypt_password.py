from cryptography.fernet import Fernet
import getpass

def generate_key():
    """ Generate and save an encryption key. """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as 'secret.key'.")

def encrypt_password():
    """ Encrypt user-provided email password. """
    password = getpass.getpass("Enter your email password: ")

    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())

    with open("encrypted_password.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_password)

    print("Password encrypted and saved as 'encrypted_password.txt'.")

if __name__ == "__main__":
    generate_key()
    encrypt_password()
