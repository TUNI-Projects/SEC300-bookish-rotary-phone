import lipsum
from t2 import T2
from cryptography.fernet import Fernet, InvalidToken


class T3:

    def __init__(self) -> None:
        self.t2 = T2()
        self.FILENAME = "lipsum.data"
        self.ENCRYPTED_FILE = "encrypted_data.data"
        self.DECRYPTED_FILE = "decrypted_data.data"
        self.ENCRYPTION_INFO = "super_secure_database.txt"

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
            file_data = file.read()
            
            # symmetric key 
            key = Fernet.generate_key()
            encrypted_data = Fernet(key).encrypt(file_data.encode())
            
            with open(self.ENCRYPTED_FILE, "wb") as encryption_file:
                encryption_file.write(encrypted_data)
            
            with open(self.ENCRYPTION_INFO, "w") as super_secret_data:
                try:
                    super_secret_data.write("{} {}".format(username, key.decode())) # decode error
                    print("----------------------------------")
                    print("File Encrypted Successfully in {}".format(self.ENCRYPTED_FILE))
                    print("----------------------------------")  
                except AttributeError as ae:
                    print(ae)
                    print("Encryption failed! Error occurred!")
                      
            
    
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
        
        secret_info = None
        with open(self.ENCRYPTION_INFO, "r") as secret_data:
            secret_info = secret_data.read()
        
        secret_info = secret_info.split(" ")
        if secret_info [0] != username:
            print("username not found in the secret database. Decryption failed!")
            return

        try:
            key = secret_info[1].encode() # encode error
        except AttributeError as ae:
            print()
            print("Decryption failed! Corrupted Key!")
            return
        
        with open(self.ENCRYPTED_FILE, 'rb') as encrypted_file:
            encrypted_message = encrypted_file.read()
            
            try:
                decrypted_message = Fernet(key).decrypt(encrypted_message).decode() # decode error
            except InvalidToken as ie:
                print()
                print("Decryption failed! Corrupted Key")
                return
            except AttributeError as ae:
                print()
                print("Decryption failed! Error occurred!")
                return
            
            with open(self.DECRYPTED_FILE, 'w') as decrypted_file:
                decrypted_file.write(decrypted_message)
                print("----------------------------------")
                print("Successfully decryption file into {}".format(self.DECRYPTED_FILE))
                print("----------------------------------")
                
    
    def main(self) -> None:
        """
        main func
        """
        while (True):
            choice = input("Type 1 for encrypt, Type 2 for decrypt >> ")
            
            if choice == "1":
                self.generate_lipsum()
                self.encrypt()
                break
            elif choice == "2":
                self.decrypt()
                break
            else:
                print("Wrong choice: {}. Try again!".format(choice))
                break


if __name__ == "__main__":
    T3().main()
