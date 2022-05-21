from random import randint


class SavingsAccount:
    account_number = randint(000000000, 999999999)
    opening_balance = 0
    balance = 0
    deposit = 0
    withdraw = 0

    def __init__(self, opening_balance) -> None:
        self.balance = opening_balance
        print(f"Your Savings Account Number is {self.account_number}")

    def deposit_money(self, amount):
        self.balance = amount

    if deposit != 0:
        deposit_money(deposit)
