import lipsum
from datetime import datetime
from t2 import T2
from Crypto.Cipher import AES


class T3:

    def __init__(self) -> None:
        self.NOW = datetime.now()
        self.DATA_FILENAME = None
        self.t2 = T2()

    def generate_lipsum(self) -> None:
        """
        will create a file, then generate lipsum
        finally will add the filename at global val
        """
        filename = "lipsum_{}.data".format(self.NOW.strftime("%d_%b_%H_%M_%S"))
        with open(filename, "w") as file:
            # this will create a file if not exist
            data = lipsum.generate_paragraphs(10)
            file.writelines(data)
            self.DATA_FILENAME = filename

    def encrypt(self):
        """
        encrypt after successful authentication
        """
        status = self.t2.login()

        if not status:
            print("User authentication failed!")
            return
        
        with open(self.DATA_FILENAME, 'r') as file:
            everything = file.read()
            key = input("Secret Encryption key: ")
            if len(key) < 16:
                print("Key must be 16 chars at least")
                return
            cipher = AES.new(key.encode(), AES.MODE_EAX)
            nonce = cipher.nonce
            encrypted_data, tag = cipher.encrypt_and_digest(everything)
            print(encrypted_data)
            print(tag)
            print(nonce)
    
    def main(self) -> None:
        """
        main func
        """
        self.generate_lipsum()
        self.encrypt()
            
        


if __name__ == "__main__":
    T3().main()
