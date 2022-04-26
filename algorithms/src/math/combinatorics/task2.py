# Ск-ми сп-ми можно уплатить сумму n монетами args. (порядок важен)
def task1(n, *args):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for arg in args:
        result += task1(n-arg, *args)
    return result


# n - баллов, k-экзаменов, args-баллы за экзамены. (порядок важен)
def task2(n, k, *args):
    if n < 0 or n == 0 and k != 0:
        return 0
    if n == 0 and k == 0:
        return 1
    result = 0
    for arg in args:
        result += task2(n-arg, k-1, *args)
    return result


# n - сумма, args-монеты. Каждой монеты лишь один вид. Ск-ко способов уплатить?
def task3(n, *args):
    if not args and n != 0 or n < 0:
        return 0
    if n == 0:
        return 1
    new_args = args[:-1]
    return task3(n, *new_args) + task3(n-args[-1], *new_args)


def task4(n, quantity_prices):
    if n < 0 or not quantity_prices and n != 0:
        return 0
    if n == 0:
        return 1
    updated_quantity_prices = quantity_prices[:-1]
    return sum([task4(n - i * quantity_prices[-1][1], updated_quantity_prices) for i in range(quantity_prices[-1][0] + 1)])


# n - сумма, args-номиналы монет (кол-во не ограничено)
def task5(n, *args):
    if not args and n != 0 or n < 0:
        return 0
    if n == 0:
        return 1
    return task5(n, *args[:-1]) + task5(n-args[-1], *args)


# Кол-во способов разбить n, на слагаемые от 1 до k (каждое из них различно)
def task6(n, k):
    if n < 0 or k == 0 and n != 0:
        return 0
    if n == 0:
        return 1
    return task6(n, k-1) + task6(n-k, k-1)
