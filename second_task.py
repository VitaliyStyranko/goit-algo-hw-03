import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > max - min + 1:
        return []

    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    return sorted(list(numbers))


min_num = 1
max_num = 49
quantity_result = 6
result = get_numbers_ticket(min_num, max_num, quantity_result)
print(result)