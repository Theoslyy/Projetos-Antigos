class MyAtm:
    def __init__(self):
        self.u = 100

    def atm(self):
        print("Welcome to CS Bank. You must enter your pin to continue.")
        self.enter_pin()
        print("Have a nice day!")

    def check_balance(self):
        print("Your balance is $",self.u)

    def withdraw(self):
        w = int(input("How much money would you like to withdraw?"))
        while w > self.u:
            print("You don't have enough to withdraw, try another value.")
            w = int(input("How much money would you like to withdraw?"))
        self.u = (self.u - w)
        print("Your balance is $",self.u)

    def deposit(self):
        print('deposit')
        d = int(input("How much money would you like to deposit?"))
        self.u = (self.u + d)
        print("Your balance is $", self.u)

    def __route(self):
        z = input("Type w to withdraw, d to deposit, or c to check balance:")
        while not (z == "c" or z == "w" or z == "d"):
            print("Invalid entry.")
            z = input("Type w to withdraw, d to deposit, or c to check balance:")
        if z == "c":
            self.check_balance()
        if z == "w":
            self.withdraw()
        if z == "d":
            self.deposit()
        b = input("Would you like to make another transaction? Type yes or no:")
        if b == "yes":
            self.__route()
       
    def enter_pin(self):
        x = int(input("Enter pin number:"))
        y = 3
        while not (x == 1234 or y == 1):
            y = y-1
            print("Incorrect. You have",y,"attempt(s) remaining.")
            x = int(input("Enter pin number:"))
        if y == 1 and not x == 1234:
            print("Try again later.")
        if x == 1234:
            self.__route()

MyAtm().atm()

