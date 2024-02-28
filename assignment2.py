from datetime import datetime 

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []
        self.__create_transaction("deposit", balance)

    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.__create_transaction("withdraw", amount)
            return f"Success. Your balance is: R{self.balance:,}"
        else:
            return f"Unsuccessful. Insufficent funds. Your Balance is: R{self.balance:,}"

    def deposit(self, amount):
        self.balance += amount
        self.__create_transaction("deposit", amount)
        return f"Success. Your balance is: R{self.balance:,}"

    def __create_transaction(self, type, amount):
        if len(self.transactions) > 0:
            id = self.transactions[-1].get("id", 0) + 1
        else:
            id = 1
        self.transactions.append(
            {"id": id, "Date": datetime.now(), "Type": type, "Amount": amount}
        )

    def print_transactions(self):
        statment = f"{'id':>6} {'Date':>5} {'Type':>6} {'Amount':>10}"
        for i, transaction in enumerate(self.transactions):
            statment = (
                statment
                + f"\n {i}. {transaction['id']:^3} {transaction['Date']:%d %b}"
                + f" {transaction['Type']:^8} {transaction['Amount']:<7,}"
            )
        return statment



caleb1 = Bank(125, "Caleb Potts", 100_000)

print('withdraw R102,000')
print(caleb1.withdraw(102_000))

print('withdraw R2,000')
print(caleb1.withdraw(2_000))

print('deposit R4,000')
print(caleb1.deposit(4_000))

print('deposit R10,000')
print(caleb1.deposit(10_000))

print('withdraw R6,000')
print(caleb1.withdraw(6_000))

print()
print(caleb1.print_transactions())