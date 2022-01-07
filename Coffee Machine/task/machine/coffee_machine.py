def print_state(water, milk, beans, cups, money):
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'${money} of money' if money != 0 else '0 of money')


def check_espresso(water, milk, beans, cups, money):
    if water >= 250 and beans >= 16 and cups >= 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
        print('I have enough resources, making you a coffee!')
    elif water < 250:
        print('Sorry, not enough water!')
    elif beans < 16:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cup!')
    return water, milk, beans, cups, money


def check_latte(water, milk, beans, cups, money):
    if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
        print('I have enough resources, making you a coffee!')
    elif water < 350:
        print('Sorry, not enough water!')
    elif milk < 75:
        print('Sorry, not enough milk!')
    elif beans < 20:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cup!')
    return water, milk, beans, cups, money


def check_cappuccino(water, milk, beans, cups, money):
    if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
        print('I have enough resources, making you a coffee!')
    elif water < 200:
        print('Sorry, not enough water!')
    elif milk < 100:
        print('Sorry, not enough milk!')
    elif beans < 12:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cup!')
    return water, milk, beans, cups, money


def buy_effect(water, milk, beans, cups, money):
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    coffee_type = int(input())
    if coffee_type == 1:
        return check_espresso(water, milk, beans, cups, money)
    elif coffee_type == 2:
        return check_latte(water, milk, beans, cups, money)
    elif coffee_type == 3:
        return check_cappuccino(water, milk, beans, cups, money)
    else:
        return None


def fill_effect(water, milk, beans, cups, money):
    print('Write how many ml of water you want to add:')
    add_water = int(input())
    water += add_water
    print('Write how many ml of milk you want to add:')
    add_milk = int(input())
    milk += add_milk
    print('Write how many grams of coffee beans you want to add:')
    add_beans = int(input())
    beans += add_beans
    print('Write how many disposable coffee cups you want to add:')
    add_cups = int(input())
    cups += add_cups
    return water, milk, beans, cups, money


def take_effect(water, milk, beans, cups, money):
    print(f'I gave you ${money}')
    money = 0
    return water, milk, beans, cups, money


def main():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action == 'buy':
            try:
                water, milk, beans, cups, money = buy_effect(water, milk, beans, cups, money)
            except ValueError:
                continue
        elif action == 'fill':
            water, milk, beans, cups, money = fill_effect(water, milk, beans, cups, money)
        elif action == 'take':
            water, milk, beans, cups, money = take_effect(water, milk, beans, cups, money)
        elif action == 'remaining':
            print_state(water, milk, beans, cups, money)
        elif action == 'exit':
            exit(0)


if __name__ == '__main__':
    main()
