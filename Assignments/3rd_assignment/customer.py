class Customer:
    name = ""
    age = 18
    nid = 0
    address = ""
    __balance = 0

    # Other Variables

    temp1, temp2, temp3, temp4 = "", 18, 0, ""
    __savingsAcc = None

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
        if command == "":
            print("There is no Command")

        elif command.lower() == 'help':
            print("""
=== Bank Account Management System Help ===
    help                   --  This Help Window.
    update info            --  Updates Your Info to a new one.
    create savings account --  Create a Savings Account.
    revert info            --  Revert your Changed Info.
    show info              --  Shows your Bank Account Details such as current balance, NID and name.
    deposit                --  Deposits your money to your Account.
    deposit savings        --  Deposits money to your Savings Account
    withdraw               --  Withdraws your money.
    withdraw savings       --  Withdraws from your Saving Account.
    exit                   --  Exits The Application.
""")

        elif command.lower() == 'update info':
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

        elif command.lower() == 'create savings account':
            if self.__savingsAcc != None:
                print("You already have a Savings Account.")
                return
            if self.__balance < 10000:
                print(
                    f"You don't have enough balance on your account to open a savings account. Required Minimum = 10,000 BDT, Your Balance = {self.__balance}")
            else:
                amount = 10000
                amount = int(
                    input("Enter how much you want as the opening amount [10000]: "))
                self.__balance -= amount
                from accounts import SavingsAccount
                self.__savingsAcc = SavingsAccount(amount)
        elif command.lower() == 'revert info':
            ubci = input(
                "Are you sure you want to revert your accounts info to the previous one? If yes, type 'yes'. anything else would be a no: ")
            if ubci.lower() == 'yes':
                self.name, self.age, self.nid, self.address = self.temp1, self.temp2, self.temp3, self.temp4
                print("Account Reverted to Previous Settings!")
            else:
                return

        elif command.lower() == 'show info':
            print(f"Your Name is {self.name}")
            print(f"Your NID is {self.nid}")
            print(f"Balance is {self.__balance}")
            if self.__savingsAcc != None:
                print(
                    f"Savings Account Balance is {self.__savingsAcc.balance}")

        elif command.lower() == 'deposit':
            self.deposit(int(input("How much money you want to deposit? ")))

        elif command.lower() == 'deposit savings':
            self.depositSavings(
                int(input("How much money you want to deposit to your Savings Account? ")))

        elif command.lower() == 'withdraw':
            self.withdraw(
                int(input("How much money do you want to withdraw? ")))

        elif command.lower() == 'withdraw savings':
            self.withdrawSavings(
                int(input("How much money do you want to withdraw in your Savings Account? ")))

        elif command.lower() == 'exit':
            print("Goodbye!", exit())

        else:
            print(f"The command \"{command}\" does not exist")
            return

    def deposit(self, amount):
        print(f"Depositing {amount} Taka To Main Account")
        self.__balance += amount

    def depositSavings(self, amount):
        if self.__savingsAcc == None:
            print("You don't have a Savings Account.")
            return
        else:
            print(f"Depositing {amount} Taka To Savings Account")
            self.__savingsAcc.deposit += amount

    def withdraw(self, amount):
        if (self.__balance - amount) != 0:
            warning = input(
                f"Are you sure you want to withdraw {amount} Taka from your Account? ")
            if warning == 'yes':
                print(f"Withdrawing {amount} Taka from your Bank Account")
                self.__balance -= amount

    def withdrawSavings(self, amount):
        if self.__savingsAcc == None:
            print("You don't have a Savings Account.")
        else:
            if (self.__savingsAcc.balance - amount) != 0:
                warning = input(
                    f"Are you sure you want to withdraw {amount} Taka from your Savings Account? ")
                if warning == 'yes':
                    print(
                        f"Withdrawing {amount} Taka from your Savings Account")
                    self.__savingsAcc.balance -= amount

    def __command_enterer(self):
        while True:
            try:
                command = input("=> ")
                self.__CommandsManager(command)
            except KeyboardInterrupt:
                print("\nYou exited the app with Keyboard shortcut. Goodbye!")
                exit()


class CustomerImpl(Customer):
    implementation = True


me = CustomerImpl(input("Enter Your Name: "), int(input("Enter Your Age: ")), int(
    input("Enter your NID: ")), input("Enter Your Address: "))
