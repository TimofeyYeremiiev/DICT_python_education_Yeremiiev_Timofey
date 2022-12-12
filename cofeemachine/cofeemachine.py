import enum


class CoffeeMachine:

    def __init__(self):
        self.water_count = 0
        self.milk_count = 0
        self.coffee_count = 0
        self.disposable_cups = 0
        self.earned_money = 0

    def handle_command(self, command: str):
        match command:
            case "buy":
                self.buy()
            case "fill":
                self.fill()
            case "take":
                self.take()
            case "remaining":
                self.remaining()
            case "exit":
                return "exit"
        return 0

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        ct = input(">")
        if not ct.isnumeric():
            return
        ct = int(ct)

        print("Write how many cups of coffee you will need:")
        cups_count = int(input(">"))

        price_list = {1: [0, 16, 250, 4], 2: [75, 20, 350, 7], 3: [100, 12, 200, 6]}
        elements = min(list([self.milk_count // price_list[ct][0],
                             self.coffee_count // price_list[ct][1],
                             self.water_count // price_list[ct][2],
                             self.disposable_cups // 1]))

        if elements >= cups_count:
            self.milk_count -= price_list[ct][0] * cups_count
            self.coffee_count -= price_list[ct][1] * cups_count
            self.water_count -= price_list[ct][2] * cups_count
            self.disposable_cups -= cups_count
            print("Succesfull")
            self.earned_money += price_list[ct][3] * cups_count
        else:
            print(f"No, I can make only {int(elements)} cups of this coffee")
        pass

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water_count += float(input(">"))
        print("Write how many ml of milk you want to add:")
        self.milk_count += float(input(">"))
        print("Write how many grams of coffee beans you want to add:")
        self.coffee_count += float(input(">"))
        print("Write how many disposable coffee cups you want to add:")
        self.disposable_cups += float(input(">"))
        print("")
        self.remaining()

    def take(self):
        if self.earned_money != 0:
            print(f"I gave you {self.earned_money}")
        else:
            print("I gave you nothing.")
        self.earned_money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water_count} of water")
        print(f"{self.milk_count} of milk")
        print(f"{self.coffee_count} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.earned_money} of money\n")


coffee_machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    task = input(">")
    if coffee_machine.handle_command(task) == "exit":
        break

