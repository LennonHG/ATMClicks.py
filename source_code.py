# ATM by Lennon 

class ATM:
    def __init__(self, name, password, saveword):
        self.name = name 
        self.password = password
        self.saveword = saveword
        
    def get_password(self):
        return self.password
    
    def get_saveword(self):
        return self.saveword
        
print("Welcome to ATMClicks")
print("If you are a new user please press 1 to sign up")
print("If you are an existing user press 2 to sign in")

answer = input()

if answer == "1":
    print("Welcome New user")
    print("Please enter your name, password and saveword below")
    
    user1 = ATM(input("Name:"), input("Password: "), input("saveword: "))
    
print(user1.get_saveword())



    
