from random import random


class Customer:
    name = ""
    age = 18
    nid = random()
    address = ""

    # Other Variables

    temp1, temp2, temp3, temp4 = "", 18, 0, ""
    system = None

    def __init__(self, name, age, nid, address):
        if age < 18:
            print("Sorry, You are not eligible to open a bank account.")
            return
        else:
            self.name = name
            self.age = age
            self.nid = nid
            self.address = address
            self.temp1, self.temp2, self.temp3, self.temp4 = self.name, self.age, self.nid, self.address

            if self.nid == nid:
                self.system = Customer("", 18, 0, "")
            print(f"Hi {self.name}, This is your CLI Bank Account Management System, Type your command below. PS: Type 'help' for commands")
            self.system.__command_enterer()

    def updateInfo(self):
        print("Update Your Info, Enter your New Details below:")
        for i in range(4):
            if i == 1:
                self.name = str(input("Enter your New Name: "))
            if i == 2:
                self.age = int(input("Enter your New Age: "))
            if i == 3:
                self.nid = int(input("Enter your New NID: "))
            if i == 4:
                self.address = str(input("Enter your New Address: "))
        print("Your Account Information Updated Succesfully! To Revert Action Type 'revert info'")

    def openSavingsAccount(self):
        from accounts import SavingsAccount
        savingsAcc = SavingsAccount()

    def revert_account(self):
        if input("Are you sure you want to revert your accounts info to the previous one? If yes, type 'yes'. anything else would be a no: ") == "yes":
            self.name, self.age, self.nid, self.address = self.temp1, self.temp2, self.temp3, self.temp4
        else:
            return

    def __CommandsManager(self, command=""):
        if command == "":
            print("There is no Command")
        elif command.lower == 'help' or '?':
            print("""
            === Bank Account Management System Help ===
            ?, help                --  This Help Window.
            update info            --  Updates Your Info to a new one.
            create savings account --  Create a Savings Account.
            revert info            --  Revert your Changed Info
            show info              --  Shows your Bank Account Details such as current balance, NID and name
            delete account         --  Deletes your Account
            """)
        elif command.lower == 'update info':
            system.updateInfo()
        elif command.lower == 'create savings account':
            system.openSavingsAccount()
        elif command.lower == 'revert info':
            system.revert_account()

    def __command_enterer():
        for i in range(999):
            global input
            input = str(input("=> "))
            system.__CommandsManager(input)


class CustomerImpl(Customer):
    implementation = True


me = Customer("Afif", 18, 19900399, "Shorashak")
