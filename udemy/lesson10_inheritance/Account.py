class Account:

    def __init__(self, acct_number, balance):
        self.acct_number = acct_number
        self.balance = balance

    def __str__(self):
        return "Account number: " + str(self.acct_number) + "\n" + \
               "Balance: " + str(self.balance)


class Checking(Account):

    def __init__(self, acct_number, balance, fee):
        Account.__init__(self, acct_number, balance)
        self.fee = fee

    def __str__(self):
        ret_str = "Account type: Checking\n"
        ret_str += Account.__str__(self)
        return ret_str

    def get_fee(self):
        return self.fee

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount - self.fee

ca = Checking("123", 500, .50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(200)
print(ca)
