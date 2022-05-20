class Customer:
    name = ""
    age = 18
    nid = 0
    address = ""

    # Other Variables

    temp1, temp2, temp3, temp4 = "", 18, 0, ""

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

            print(f"Hi {self.name}, This is your CLI Bank Account Management System, Type your command below. PS: Type 'help' for commands")
            self.__command_enterer()

    def __CommandsManager(self, command=""):
        if command.lower() == 'help':
            print("""
=== Bank Account Management System Help ===
help                --  This Help Window.
update info            --  Updates Your Info to a new one.
create savings account --  Create a Savings Account.
revert info            --  Revert your Changed Info.
show info              --  Shows your Bank Account Details such as current balance, NID and name.
delete account         --  Deletes your Account.
exit                   --  Exits The Application.
""")

        if command.lower() == 'update info':
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
            print(
                "Your Account Information Updated Succesfully! To Revert Action Type 'revert info'")
            return

        if command.lower() == 'create savings account':
            from accounts import SavingsAccount
            global __savingsAcc
            __savingsAcc = SavingsAccount()
            return

        if command.lower() == 'revert info':
            ubci = input(
                "Are you sure you want to revert your accounts info to the previous one? If yes, type 'yes'. anything else would be a no: ")
            if ubci.lower == 'yes':
                self.name, self.age, self.nid, self.address = self.temp1, self.temp2, self.temp3, self.temp4
            else:
                return

        if command.lower() == 'show info':
            print(f"Your Name is {self.name}")
            print(f"Your NID is {self.nid}")
            print(f"Balance is {__savingsAcc.opening_balance}")
            return

        if command.lower() == 'deposit money':
            self.deposit(input("How much money you want to deposit? "))
            return

        if command.lower() == 'exit':
            print("Goodbye!")
            exit()

        if command == "":
            print("There is no Command")
            return

        else:
            print(f"The command \"{command}\" does not exist")
            return

    def deposit(self, amount):
        print(f"Depositing {amount} Taka To Savings Account")
        __savingsAcc.deposit = amount

    def __command_enterer(self):
        for i in range(999999):
            command = input("=> ")
            self.__CommandsManager(command)


class CustomerImpl(Customer):
    implementation = True


me = Customer("Afif", 18, 19900399, "Shorashak")
