class CoffeeMachine:
    def __init__(self, init_money, init_water, init_milk, init_beans, init_cups):
        self.init_money = init_money
        self.init_water = init_water
        self.init_milk = init_milk
        self.init_beans = init_beans
        self.init_cups = init_cups

    def buy_function(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if choice == "1":
            if self.init_water < 250:
                print("Sorry, not enough water!")
            elif self.init_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.init_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.init_money += 4
                self.init_water -= 250
                self.init_beans -= 16
                self.init_cups -= 1
        elif choice == "2":
            if self.init_water < 350:
                print("Sorry, not enough water!")
            elif self.init_milk < 75:
                print("Sorry, not enough milk!")
            elif self.init_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.init_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.init_money += 7
                self.init_water -= 350
                self.init_milk -= 75
                self.init_beans -= 20
                self.init_cups -= 1
        elif choice == "3":
            if self.init_water < 200:
                print("Sorry, not enough water!")
            elif self.init_milk < 100:
                print("Sorry, not enough milk!")
            elif self.init_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.init_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.init_money += 6
                self.init_water -= 200
                self.init_milk -= 100
                self.init_beans -= 12
                self.init_cups -= 1
        elif choice == "back":
            pass

    def fill_function(self):
        add_water = int(input("Write how many ml of water do you want to add:"))
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        add_beans = int(input("Write how many grams of coffee do you want to add:"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.init_water += add_water
        self.init_milk += add_milk
        self.init_beans += add_beans
        self.init_cups += add_cups


    def take_function(self):
        print("I gave you $" + str(self.init_money))
        self.init_money = 0

    def remain_function(self):
        print()
        print("The coffee machine has:")
        print(str(self.init_water) + " of water")
        print(str(self.init_milk) + " of milk")
        print(str(self.init_beans) + " of coffee beans")
        print(str(self.init_cups) + " of disposable cups")
        print("$" + str(self.init_money) + " of money")

coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)

option = input("Write action (buy, fill, take, remaining, exit):")

while option != "exit":
    if option == "buy":
        coffee_machine.buy_function()
    elif option == "fill":
        coffee_machine.fill_function()
    elif option == "take":
        coffee_machine.take_function()
    elif option == "remaining":
        coffee_machine.remain_function()
    option = input("Write action (buy, fill, take, remaining, exit):")


