class User:
    def __init__(self, id_user, username, password, rekening, balance):
        self.__id_user = id_user
        self.__username = username
        self.__password = password
        self.__rekening = rekening
        self.__balance = balance
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_rekening(self):
        return self.__rekening
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Berhasil deposit: Rp{amount}. Saldo sekarang: Rp{self.__balance}")
        else:
            print("Gagal! Jumlah deposit harus lebih besar dari 0!")
            
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Gagal! Jumlah penarikan harus lebih besar dari 0.")
        elif amount > self.__balance:
            print("Gagal! Saldo tidak mencukupi.")
        else:
            self.__balance -= amount
            print(f"Berhasil tarik tunai: Rp{amount}. Saldo sisa: Rp{self.__balance}")

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
        
        user_baru = User(user_id, username_input, password_input, rekening, balance_input)
        
        self.__user_database[username_input] = user_baru
        
        print(f"Registrasi berhasil! Nomor rekening Anda: {rekening}, sebagai review awal:")
        
    def login(self, username, password):
        print("\n=== LOGIN ===")
        username = input("Username: ")
        password = input("password: ")
        
        if username in self.__user_database:
            user = self.__user_database[username]
            if user.get_password() == password:
                print("Login berhasil!")
                return user
        
        print("Username atau password salah!")
        return None
    
bank = Bank()
current_user = None

while True:
    if current_user is None:
        print("\n=== ATM AlexaBank ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            bank.register()
        elif pilihan == "2":
            bank.login()
        elif pilihan == "3":
            break
    else:
        print(f"\n--- Selamat Datang, {current_user.get_username()} ---")
        print("1. Cek Saldo")
        print("2. Logout")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            print(f"Saldo Anda: Rp{current_user.get_balance()}")
        elif pilihan == "2":
            current_user = None
            print("Anda telah logout.")