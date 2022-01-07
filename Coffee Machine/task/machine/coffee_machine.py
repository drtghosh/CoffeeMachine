class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        machine_state = 'The coffee machine has:\n'
        machine_state += f'{self.water} of water\n'
        machine_state += f'{self.milk} of milk\n'
        machine_state += f'{self.beans} of coffee beans\n'
        machine_state += f'{self.cups} of disposable cups\n'
        machine_state += f'${self.money} of money' if self.money != 0 else '0 of money'
        return machine_state

    def check_espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print('I have enough resources, making you a coffee!')
        elif self.water < 250:
            print('Sorry, not enough water!')
        elif self.beans < 16:
            print('Sorry, not enough coffee beans!')
        elif self.cups < 1:
            print('Sorry, not enough cup!')

    def check_latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            print('I have enough resources, making you a coffee!')
        elif self.water < 350:
            print('Sorry, not enough water!')
        elif self.milk < 75:
            print('Sorry, not enough milk!')
        elif self.beans < 20:
            print('Sorry, not enough coffee beans!')
        elif self.cups < 1:
            print('Sorry, not enough cup!')

    def check_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
            print('I have enough resources, making you a coffee!')
        elif self.water < 200:
            print('Sorry, not enough water!')
        elif self.milk < 100:
            print('Sorry, not enough milk!')
        elif self.beans < 12:
            print('Sorry, not enough coffee beans!')
        elif self.cups < 1:
            print('Sorry, not enough cup!')

    def buy_effect(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee_type = int(input())
        if coffee_type == 1:
            self.check_espresso()
        elif coffee_type == 2:
            self.check_latte()
        elif coffee_type == 3:
            self.check_cappuccino()
        else:
            raise ValueError

    def fill_effect(self):
        print('Write how many ml of water you want to add:')
        added_water = int(input())
        self.water += added_water
        print('Write how many ml of milk you want to add:')
        added_milk = int(input())
        self.milk += added_milk
        print('Write how many grams of coffee beans you want to add:')
        added_beans = int(input())
        self.beans += added_beans
        print('Write how many disposable coffee cups you want to add:')
        added_cups = int(input())
        self.cups += added_cups

    def take_effect(self):
        print(f'I gave you ${self.money}')
        self.money = 0


def main():
    coffee_machine = CoffeeMachine()
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action == 'buy':
            try:
                coffee_machine.buy_effect()
            except ValueError:
                continue
        elif action == 'fill':
            coffee_machine.fill_effect()
        elif action == 'take':
            coffee_machine.take_effect()
        elif action == 'remaining':
            print(coffee_machine)
        elif action == 'exit':
            exit(0)


if __name__ == '__main__':
    main()
