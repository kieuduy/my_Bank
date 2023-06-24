import random

class Bank:
    def __init__(self):
        self.initial_money = 5
        self.account_survival = []
        self.bank_account = {}

    # MENU
    print("Welcome To Our Bank!")
    def menu(self):
        print("\nMENU")
        print("(1) Create New Acount")
        print("(2) Operation")
        print("(3) Exit")
        print(self.account_survival)
        choice = int(input("You choose: "))
        if choice == 1:
            self.sign_up()
        if choice == 2:
            self.Into_account()
        if choice == 3:
            print("Thanks and Goodbye!")
            exit()

    # SIGN UP(1)
    def sign_up(self):
        test = True
        customer_name = input("Enter your name: ")
        customer_address = input("Enter your address: ")
        customer_phone = input("Enter your phone number: ")
        customer_password = input("\nEnter your password: ")
        # Check if retype password are similar, then push all information a dict
        while test == True:
            retype_pass = input("Retype your password: ")
            if retype_pass == customer_password:
                account_number = random.randint(1, 100)
                self.account_survival.append(account_number)
                print("\nBonjour {}, you have been successfully created a new account! \nYour account number is {} \nYou are provided 5$ for an initial bank account".format(customer_name, account_number))
                self.bank_account[account_number] = {
                    "Name": customer_name,
                    "Address": customer_address,
                    "Phone": customer_phone,
                    "Password": customer_password,
                    "Recent_amount": 5,
                    "Account_number": account_number,
                }
                print("\nMENU")
                self.menu()
                return self.bank_account[account_number]
                test = False
            else:
                print("False, please retype your password again!\n")

    # OPERATION
    # sign in an account and keep staying in this account to opperate
    def Into_account(self):
        account = self.Sign_in()
        self.operation(account)
    def operation(self, account):
        print("\nOPERATION")
        print("(1) Change passworld")
        print("(2) Deposit")
        print("(3) Withdraw")
        print("(4) Your file")
        print("(5) Sign out")
        choice = int(input("You choose: "))
        if choice == 1:
            self.Change_password(account["Account_number"])
            self.operation(account)
        if choice == 2:
            self.Deposit(account["Account_number"])
            self.operation(account)
        if choice == 3:
            self.Withdraw(account["Account_number"])
            self.operation(account)
        if choice == 4:
            self.file(account)
            self.operation(account)
        if choice == 5:
            print("Thanks and Goodbye!")
            self.menu()
        else:
            print(f"There aren't function ({choice})")
            self.operation(account) 

    def valid_accNumber(self, inp):
        return inp.isdigit()
    # SIGN IN
    def Sign_in(self):
        print("\nSIGN IN")
        test_acc = True
        test_numb = True
        while test_acc == True:
            while test_numb == True:
                account_number = input("Enter your account number: ")
                if self.valid_accNumber(account_number):
                    # account_number_number = int(account_number)
                    break
            if int(account_number) in self.account_survival:
                break
            else:
                print("This account does not exist\n")
        test = True
        while test == True: 
            password = input("Enter your password: ")
            if password == self.bank_account[int(account_number)]["Password"]:
                print("You have successfully signed in.")
                return self.bank_account[int(account_number)]  
                break
            else:
                print("\nYou have typed wrong password")

    # CHANGE PASSWORD
    def Change_password(self, account_number):
        new_pass = input("\nEnter your new password: ")
        while True:
            retype = input("Retype your new password: ")
            if retype == new_pass:
                print("You have successfully changed your password.")
                self.bank_account[account_number]["Password"] = new_pass
                break
            else:
                print("You have retyped wrong!")

    # DEPOSIT
    def Deposit(self, account_number):
        test_numb = True
        print("\nYour initial balance is {:,}$".format(self.bank_account[account_number]["Recent_amount"])) 
        while test_numb == True:
            deposit_amount = int(input("Enter your deposit amount($): "))
            if self.valid_accNumber(deposit_amount):
                break
            else:
                print("Your input is invalid, please type again!")
        self.bank_account[account_number]["Recent_amount"] += deposit_amount
        print("Your recent balance is {:,}$".format(self.bank_account[account_number]["Recent_amount"]))
        
    # WITHDRAW
    def Withdraw(self, account_number):
        print("\nYour initial balance is {:,}$".format(self.bank_account[account_number]["Recent_amount"])) 
        test_numb = True
        while test_numb == True:
            deposit_amount = int(input("Enter your withdraw amount($): "))
            if self.valid_accNumber(deposit_amount):
                break
            else:
                print("Your input is invalid, please type again!")
        if self.bank_account[account_number]["Recent_amount"] >= deposit_amount:
            self.bank_account[account_number]["Recent_amount"] -= deposit_amount
            print("Your recent balance is {:,}$".format(self.bank_account[account_number]["Recent_amount"]))
        else:
            print("You are not enough money to withdraw!")
            self.Withdraw(account_number)

    # MY ACCOUNT
    def file(self, account):
        print("\nCUSTOMER", account["Name"])
        print("Account ID:", account["Account_number"])
        print("Address:", account["Address"])
        print("Phone number:", account["Phone"])
        print("Balance:", str(account["Recent_amount"]) + "$")


if __name__ == "__main__":
    myBank = Bank()
    myBank.menu()


# NEXT STEP: Building a module