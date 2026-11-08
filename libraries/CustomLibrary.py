from enum import Enum

class CustomLibrary:

    VERSION : str= "1.0.0"

    LOGIN_USER_DATA : dict= {
        "ironman": {
            "username": "Tony Stark",
            "password": "1234567890",
        }
    }

    class State(Enum):
        DISCONNECTED = 1
        CONNECTED = 2
        LOGGED = 3

    def __init__(self):
        self.tmp_login_name : str= None
        self.tmp_password : str= None
        self.login_name : str= None
        self.username : str= None
        self.password : str= None
        self.ip : str= None
        self.state = CustomLibrary.State.DISCONNECTED

    def set_login_name(self, name: str):
        self.tmp_login_name = name

    def set_password(self, password: str):
        self.tmp_password = password

    def execute_login(self):
        if self.tmp_login_name not in CustomLibrary.LOGIN_USER_DATA.keys():
            raise ValueError("Invalid login name")

        if self.tmp_password != CustomLibrary.LOGIN_USER_DATA[self.tmp_login_name]["password"]:
            raise ValueError("Invalid Password")

        self.login_name = self.tmp_login_name
        self.password = self.tmp_password

        self.username = CustomLibrary.LOGIN_USER_DATA[self.tmp_login_name]["username"]

        self.state = CustomLibrary.State.LOGGED

        self.tmp_login_name = None
        self.tmp_password = None


    def get_username(self) -> str:
        return self.username 

    def connect(self, ip: str):
        if self.state == CustomLibrary.State.DISCONNECTED:
            self.ip = ip
            self.state = CustomLibrary.State.CONNECTED

    def disconnect(self):
        self.ip = None
        self.state == CustomLibrary.State.DISCONNECTED

    def get_server_version(self):
        if self.state != CustomLibrary.State.LOGGED:
            raise PermissionError("Cannot get server version to user not logged in")

        return CustomLibrary.VERSION
