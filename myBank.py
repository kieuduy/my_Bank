import random

# MENU
print("Welcome To Our Bank!")
def menu(bank_account, account_survival):
    print("\nMENU")
    print("(1) Create New Acount")
    print("(2) Operation")
    print("(3) Exit")
    print(account_survival)
    choice = int(input("You choose: "))
    if choice == 1:
        sign_up(bank_account, account_survival)
    if choice == 2:
        Into_account(bank_account, account_survival)
    if choice == 3:
        print("Thanks and Goodbye!")
        exit()

# SIGN UP(1)
def sign_up(bank_account, account_survival):
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
            account_survival.append(account_number)
            print("\nBonjour {}, you have been successfully created a new account! \nYour account number is {} \nYou are provided 5$ for an initial bank account".format(customer_name, account_number))
            bank_account[account_number] = {
                "Name": customer_name,
                "Address": customer_address,
                "Phone": customer_phone,
                "Password": customer_password,
                "Recent_amount": 5,
                "Account_number": account_number,
            }
            print("\nMENU")
            menu(bank_account, account_survival)
            return bank_account[account_number]
            test = False
        else:
            print("False, please retype your password again!\n")

# OPERATION
# sign in an account and keep staying in this account to opperate
def Into_account(bank_account, account_survival):
    account = Sign_in(bank_account, account_survival)
    operation(bank_account, account)
def operation(bank_account, account):
    print("\nOPERATION")
    print("(1) Change passworld")
    print("(2) Deposit")
    print("(3) Withdraw")
    print("(4) Your file")
    print("(5) Sign out")
    choice = int(input("You choose: "))
    if choice == 1:
        Change_password(bank_account, account["Account_number"])
        operation(bank_account, account)
    if choice == 2:
        Deposit(bank_account, account["Account_number"])
        operation(bank_account, account)
    if choice == 3:
        Withdraw(bank_account, account["Account_number"])
        operation(bank_account, account)
    if choice == 4:
        file(bank_account, account)
        operation(bank_account, account)
    if choice == 5:
        print("Thanks and Goodbye!")
        menu(bank_account, account_survival)
    else:
        print(f"There aren't function ({choice})")
        operation(bank_account, account) 
# SIGN IN
def Sign_in(bank_account, account_survival):
    print("\nSIGN IN")
    test_acc = True
    while test_acc == True:
        account_number = int(input("Enter your account number: "))
        if account_number in account_survival:
            break
        else:
            print("This account does not exist\n")
    test = True
    while test == True: 
        password = input("Enter your password: ")
        if password == bank_account[account_number]["Password"]:
            print("You have successfully signed in.")
            return bank_account[account_number]  
            break
        else:
            print("\nYou have typed wrong password")



# CHANGE PASSWORD
def Change_password(bank_account, account_number):
    new_pass = input("\nEnter your new password: ")
    while True:
        retype = input("Retype your new password: ")
        if retype == new_pass:
            print("You have successfully changed your password.")
            bank_account[account_number]["Password"] = new_pass
            break
        else:
            print("You have retyped wrong!")

# DEPOSIT
def Deposit(bank_account, account_number):
    print("\nYour initial balance is {:,}$".format(bank_account[account_number]["Recent_amount"])) 
    deposit_amount = int(input("Enter your deposit amount($): "))
    bank_account[account_number]["Recent_amount"] += deposit_amount
    print("Your recent balance is {:,}$".format(bank_account[account_number]["Recent_amount"]))
    
# WITHDRAW
def Withdraw(bank_account, account_number):
    print("\nYour initial balance is {:,}$".format(bank_account[account_number]["Recent_amount"])) 
    deposit_amount = int(input("Enter your withdraw amount($): "))
    if bank_account[account_number]["Recent_amount"] >= deposit_amount:
        bank_account[account_number]["Recent_amount"] -= deposit_amount
        print("Your recent balance is {:,}$".format(bank_account[account_number]["Recent_amount"]))
    else:
        print("You are not enough money to withdraw!")
        Withdraw(bank_account, account_number)

# MY ACCOUNT
def file(bank_account, account):
    print("\nCUSTOMER", account["Name"])
    print("Account ID:", account["Account_number"])
    print("Address:", account["Address"])
    print("Phone number:", account["Phone"])
    print("Balance:", str(account["Recent_amount"]) + "$")

bank_account = {}
account_survival = []
menu(bank_account, account_survival)



# NEXT STEP: Building a module