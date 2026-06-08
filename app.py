class User:
    def __init__(self, id, username, password, rekening, balance):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__rekening = rekening
        self.__balance = balance
    
    def get_username(self):
        return self.__username
    
    def deposit(self):
        pass

class Bank:
    def __init__(self):
        self.__user_database = {}
    
    def register(self, username, password, initial_balance):
        pass
    
    def login(self, username, password):
        pass