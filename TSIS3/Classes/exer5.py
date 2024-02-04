number = int(input("What`s your bank card number? "))
cvv = int(input("Enter your CVV code: "))
name = "Kadyr Sultan" 
# cvv = 777 and number card = 44054410

class Account:
    def __init__(self, number, cvv, name):
        self.number = number
        self.cvv = cvv
        self.name = name
    def owner(self):
        if self.cvv == 777 and self.number == 44054410:
            print ("\n""Welocome Kadyr Sultan!")
        else :
            self.name = input("\n""Welcome! Write your name: ")
            print("New member added!")
    def balance(self):
        self.balance_S = 10000
        self.balance1 = 0
        if self.cvv == 777 and self.number == 44054410:
            self.balance_S = 10000
            print("\n Your Balance: ")
            print(self.balance_S, "dollars")
        else:
            self.balance1 = 0
            print("\n Your Balance: ")
            print(self.balance1, "dollars")

    def deposit(self):
        self.answer = input("""\nDo you want to see your deposit or cash in?
Write \"See\" or \"Cash in\"
""")
        self.depo = 0
        self.deposula = 1200
        if self.answer == "See":
            if self.cvv == 777 and self.number == 44054410:
                print("\n Your Deposit: ")
                print(self.deposula, "dollars")
            else:
                print("\n Your Deposit: ")
                print(self.depo, "dollars")
        elif self.answer == "Cash in":
            if self.cvv == 777 and self.number == 44054410:
                self.deposula += int(input())
                print("\n Your Deposit: ")
                print(self.deposula)
            else:
                self.depo += int(input())
                print("\n Your Deposit: ")
                print(self.depo)
        
    def wirhdraw(self):
        print("\n")
        self.wheretake = str(input("Where you want to take money in \"Balance\" or \"Deposit?\" "))
        self.wirthDraw = int(input("How many money you want to withdrawals = "))

        if self.wheretake == "Balance":

            if self.cvv == 777 and self.number == 44054410:

                if  self.balance_S - self.wirthDraw  > -1 and self.wirthDraw > self.balance_S:
                    print("\nWithdrawals may not exceed the available balance!")
                else:
                    print("\nPlease take your money. Thanks you for using us!")
                    self.balance_S -= self.wirthDraw
                    print("\n")
                    print(self.balance_S)
 
            else:

                if self.balance1 - self.wirthDraw  > -1 and self.wirthDraw > self.balance1:
                    print("\nWithdrawals may not exceed the available balance!")
                else:
                    print("\nPlease take your money. Thanks you for using us!")
                    self.balance1 -= self.wirthDraw
                    print("\n")
                    print(self.balance1)

        elif self.wheretake == "Deposit":
            if self.cvv == 777 and self.number == 44054410:

                if self.deposula - self.wirthDraw > -1 and self.wirthDraw > self.deposula:
                    print("\nWithdrawals may not exceed the available balance!")
                else:
                    print("\nPlease take your money. Thanks you for using us!")
                    self.deposula -= self.wirthDraw
                    print("\n")
                    print(self.deposula)

            else:

                if self.depo - self.wirthDraw > -1 and self.wirthDraw > self.depo:
                    print("\nWithdrawals may not exceed the available balance!")
                else:
                    print("\nPlease take your money. Thanks you for using us!")
                    self.depo -= self.wirthDraw
                    print("\n")
                    print(self.depo)


bank = Account(number, cvv, name)
#1
bank.owner()
bank.balance()
bank.deposit()
bank.wirhdraw()
print("\n")

number = int(input("What`s your bank card number? "))
cvv = int(input("Enter your CVV code: "))
bank = Account(number, cvv, name)
print("\n")
#2
bank.owner()
bank.deposit()
bank.wirhdraw()
print("\n")

number = int(input("What`s your bank card number? "))
cvv = int(input("Enter your CVV code: "))
bank = Account(number, cvv, name)
print("\n")

#3
bank.owner()
bank.deposit()
bank.wirhdraw()

