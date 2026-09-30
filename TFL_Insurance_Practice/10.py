# Singleton

class BankVault:
    __instance =None
    def __new__(cls,*args, **kawargs):
        if cls.__instance is None:
            print("Creating the vault...")
            cls.__instance =super().__new__(cls)
            
        return cls.__instance
    def __init__(self):
        self.balance =100
            
vault1 =BankVault()
vault2 =BankVault()

vault1=BankVault()
vault1.balance += 500

print(vault2.balance)

#One simple approach is to initialize the state only when the singleton object is first created:
# class BankVault:
#     __instance =None
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance =super().__new__(cls)
#             cls.__instance.balance =100
#         return cls.__instance