class User:
    def __init__(self, id_user, username, password, rekening, balance):
        self.__id_user = id_user
        self.__username = username
        self.__password = password
        self.__rekening = rekening
        self.__balance = balance
    
    def get_username(self):
        return self.__username
    
    def deposit(self):
        pass


class Bank:
    __counter = 1
    
    def __init__(self):
        self.__user_database = {}
    
    def register(self):
        username_input = input("Masukkan username: ")
        password_input = input("Masukkan Password: ")
        balance_input = float(input("Masukkan uang anda: "))
        
        user_id = Bank.__counter
        rekening = "100" + str(user_id)
        Bank.__counter += 1
        
        self.__user_database["username"] = username_input
        self.__user_database["password"] = password_input
        self.__user_database["Balance"] = balance_input
        
        user_baru = User(user_id, username_input, password_input, rekening, balance_input)
        
        self.__user_database[username_input] = user_baru
        
        print(f"Registrasi berhasil! Nomor rekening Anda: {rekening}")
        print(self.__user_database)
        
    def login(self, username, password):
        pass
    
user1 = Bank()
user1.register()