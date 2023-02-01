import lipsum
from datetime import datetime
from t2 import T2
from Crypto.Cipher import AES


class T3:

    def __init__(self) -> None:
        self.t2 = T2()
        self.NOW = datetime.now()
        self.FILENAME = "lipsum.data"
        self.ENCRYPTED_FILE = "encrypted_data.data"
        self.DECRYPTED_FILE = "decrypted_data.data"
        
        self.ENCRYPTION_INFO = "encryption_database.data"

    def generate_lipsum(self) -> None:
        """
        will create a file, then generate lipsum
        finally will add the filename at global val
        """
        with open(self.FILENAME, "w") as file:
            # this will create a file if not exist
            data = lipsum.generate_paragraphs(10)
            file.writelines(data)

    def encrypt(self):
        """
        encrypt after successful authentication
        """
        print("---------------------------------------------")
        print("File Encryption")
        print("---------------------------------------------")
        status, username = self.t2.login()

        if not status:
            print("User authentication failed!")
            return
        
        with open(self.FILENAME, 'r') as file:
            everything = file.read()
            key = input("Secret Encryption key: ")
            if len(key) != 16:
                print("Key must be 16 chars")
                return
            cipher = AES.new(key.encode(), AES.MODE_EAX)
            nonce = cipher.nonce
            encrypted_data, tag = cipher.encrypt_and_digest(everything.encode())
            with open(self.ENCRYPTED_FILE, "wb") as encrypted_file:
                # write encrypted data on a file
                encrypted_file.write(encrypted_data)
            
            line = "{} {} {}".format(username, nonce, tag)
            
            with open(self.ENCRYPTION_INFO, "wb") as encrpt_info_file:
                # will only store last encryption information
                encrpt_info_file.write(line)
            print("File Encrypted Successfully!")            
            
    
    def decrypt(self) -> None:
        """
        decrypt a file
        """
        print("---------------------------------------------")
        print("File Decyption")
        print("---------------------------------------------")
        status, username = self.t2.login()

        if not status:
            print("User authentication failed!")
            return
        
        with open(self.ENCRYPTED_FILE, "rb") as file:
            encrypted_text = file.read()
            key = input("Secret Encryption key: ")
            if len(key) != 16:
                print("Key must be 16 chars.")
                return
            
            nonce, tag = None, None
            with open(self.ENCRYPTION_INFO, "rb") as encrpted_info:
                secret_info = encrpted_info.read()
                secret_info = secret_info.decode()
                secret_info = secret_info.split(" ")
                print(secret_info)
                if secret_info[0] != username:
                    print("decryption failed!")
                    return
                nonce, tag = secret_info[1], secret_info[2]
            
            nonce = nonce.encode()
            tag = tag.encode()
            
            print(key)
            print(nonce)
            print(tag)    
            
            cipher = AES.new(key.encode(), AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(encrypted_text)
            
            try:
                cipher.verify(tag)
                print("Decrypted successfully!")
                with open(self.DECRYPTED_FILE, "w") as decrypt_file:
                    decrypt_file.write(plaintext)
            except ValueError:
                print("Incorrect key or data corrupted!")
            
    
    def main(self) -> None:
        """
        main func
        """
        self.generate_lipsum()
        self.encrypt()
        self.decrypt()


if __name__ == "__main__":
    T3().main()
