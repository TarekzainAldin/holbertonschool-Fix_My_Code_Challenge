#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    def __init__(self):
        """
        Initialize a new user:
        - assigned a unique `id`
        - password initially None
        """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - Set `None` if `pwd` is `None` or not a string
        - Hash `pwd` in MD5 and assign to `__password`
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        Valid password:
        - Returns `False` if `pwd` is None, not a string, or password is not set
        - Compares the MD5 hash of `pwd` with the stored password
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd

    # Checking if password is hashed
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")
    else:
        print("Password is valid!")  # This should be the correct result

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
