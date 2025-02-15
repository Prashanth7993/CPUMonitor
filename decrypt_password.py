from cryptography.fernet import Fernet

def load_key():
    """ Load encryption key from file. """
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def decrypt_password():
    """ Decrypt and return stored email password. """
    key = load_key()
    cipher = Fernet(key)

    with open("encrypted_password.txt", "rb") as encrypted_file:
        encrypted_password = encrypted_file.read()

    return cipher.decrypt(encrypted_password).decode()

if __name__ == "__main__":
    print("Decrypted Password:", decrypt_password())
