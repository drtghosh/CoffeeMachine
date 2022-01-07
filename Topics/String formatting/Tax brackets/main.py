def calculate_tex(amount, percent):
    return round(amount * percent / 100)


def get_percent(amount):
    if 0 <= amount < 15528:
        return 0
    elif amount < 42708:
        return 15
    elif amount < 132407:
        return 25
    else:
        return 28


income = int(input())
percentage = get_percent(income)
tax = calculate_tex(income, percentage)
print(f'The tax for {income} is {percentage}%. That is {tax} dollars!')