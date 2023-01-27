import bcrypt
import re


class T2:
    """
    Exercise 2 (2 points): Implement a program that authenticates a user with a user name and password. 
    Hashes of passwords are stored in a file. Please notice to use random salt.
    """

    def __init__(self) -> None:
        self.FILENAME = "the_big_database.data"
        self.DATA_FORMAT = "{} {}"

    def file_write(self, data: dict) -> None:
        """_summary_

        Args:
            data (dict): _description_
        """
        with open(self.FILENAME, "a") as file:
            line = self.DATA_FORMAT.format(data["username"], data["password"])
            file.write(line)

    def check_if_exist(self, username: str) -> str:
        """_summary_

        Args:
            username (str): _description_
        """
        with open(self.FILENAME, 'r') as file:
            all_lines = file.readlines()

            for line in all_lines:
                if line.split(" ")[0] == username:
                    return line.split(" ")[1]
            return None

    def login(self) -> tuple:
        """_summary_
        basic authenticatioN!
        this func will be used to enc/dec in task 3.
        
        Returns:
            (bool, str): for t3
        """
        print("Dummy user authentication")
        username = input("username >> ")
        password = input("password >> ")

        # username sanitation, [a-zA-Z0-9]
        if not re.match("^[A-Za-z0-9]*$", username):
            print("Invalid Username")
            return False, None

        hashed_password = self.check_if_exist(username)
        if hashed_password is None:
            print("Invalid Username!")
            return False, None
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            print("Password matched! User authenticated. :)")
            return True, username
        else:
            print("Incorrect password!")
            return False, None

    def register(self)-> None:
        """
        register username, password and write it on a file.
        """
        print("Dummy user registration")
        username = input("username >> ")
        password = input("password >> ")

        # username sanitation, [a-zA-Z0-9]
        if not re.match("^[A-Za-z0-9]*$", username):
            print("Invalid Username, valid > A-Za-z0-9")
            return

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.file_write({
            "username": username,
            "password": hashed.decode()
        })
    
    def main(self) -> None:
        choice = input("1 for register, 2 for login: ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        else:
            print("Unknown option!")


if __name__ == "__main__":
    T2().main()
