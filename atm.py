class Atm:
    def __init__(self, cardNum, PIN):
        self.money = 10000
        self.cardNum = cardNum
        self.PIN = PIN
    def withdraw(self, amount):
        self.money -= amount
        print("You have withdrawn ", amount, "$. Your new balance is ", self.money, "$.")
    def mybalance(self):
        print("Your balance is ", self.money, "$.")
    def deposit(self, amount):
        self.money += amount
        print("You have deposited ", amount, "$. Your new balance is ", self.money, "$.")
atm = Atm(200020002000, 1234)
atm.mybalance()
atm.withdraw(int(input("How much would you like to withdraw? ")))
atm.deposit(int(input("How much would you like to deposit? ")))