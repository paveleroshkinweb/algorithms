from utils import placements_with_repetitions, placements, permutations, combinations, permutations_with_repetitions


# Сколько членов было в клубе, если известно,
# что использованы все n значные номера, не содержащие ни одной 8?
def task1(n):
    return placements_with_repetitions(n, 9)


# Сколько в n-ичной системе счисления чисел, записываемых ровно k знаками?
def task2(n, k):
    return (n - 1) * placements_with_repetitions(k-1, n)


# Пусть на диск наненесены n букв, а секретное слово состоит из k букв.
# Сколько неудачных попыток может быть сделано?
def task3(n, k):
    return placements_with_repetitions(k, n) - 1


# Сколькими способами из 28 костей домино можно выбрать 2 кости так,
# чтобы их можно было приложить друг к другу?
def task4():
    return 6 * 7 + 21 * 5


# Учавствуют 17 команд. Ск-ми сп-ми можно распределить медали
def task5():
    return placements(17, 3)


# Ск-ми способами можно расположить n ладей, на n*n доске, что б они не били друг друга?
def task6(n):
    return permutations(n)


# n девушек водят хоровод. Ск-ми способами они могут встать в круг?
def task7(n):
    return permutations(n-1)


# Ск-ми способами можно поставить n ладей на n*n доску?
def task8(n):
    return combinations(n * n, n)


# Есть k сорта пирожных. Ск-ми способами можно купить n пирожных?
def task9(n, k):
    return combinations(n+k-1, k-1)


# Есть n львов и k тигров. (отличимых друг от друга) Нельзя чтобы 2 тигра шли друг за другом.
# Ск-ми способами их можно вывести ?(n>=k)
def task10(n, k):
    return permutations(n) * placements(n+1, k)


# Ск-ми способами можно расставить n нулей и k единиц так, чтобы никакие 2 единицы
# не стояли рядом?
def task11(n, k):
    return combinations(n+1, k)


# На книжной полке 12 книг. Ск-ми сп-ми можно выбрать 5, чтобы никакие 2 не стояли рядом?
def task12():
    return task11(7, 5)


# За круглым столом сидит n рыцарей. Каждый воюет со своими соседями. Надо выбрать k рыцырей,
# что бы среди них не было врагов? (k <= n/2)
def task13(n, k):
    return combinations(n-k, k) + combinations(n-k-1, k-1)


# Берутся все перестановки из n различных чисел,
# в скольки случаих ни одно не стоит на своем месте?
def task14(n):
    result = permutations(n)
    for i in range(1, n+1):
        result += (-1) ** i * combinations(n, i) * permutations(n-i)
    return result


# Берутся все перестановки из n различных чисел, в сколько случаях ровно
# k остаются на своих местах, а остальные перемешаны
def task15(n, k):
    return combinations(n, k) * task14(n - k)


# Число перестановок из n различных чисел с поторениями,
# при которых ни один не стоит на своем месте?
def task16(n):
    return (n - 1) ** n


# Число перестановок при которых данные k элементов смещены,
# а остальные могут быть как смещены так и нет?
def task17(n, k):
    result = permutations(n)
    for i in range(1, k+1):
        result += (-1) ** i * combinations(k, i) * permutations(n-i)
    return result


# Идет караван из n верблюдов. Ск-ми сп-ми можно их переставить,
# чтобы перед каждым шел другой верблюд?
def task18(n):
    result = permutations(n)
    for i in range(1, n):
        result += (-1) ** n * combinations(n-1, i) * permutations(n-i)
    return result


# Карусель n ребят. Ск-ми сп-ми их можно пересадить,
# чтобы перед каждым шел другой?
def task19(n):
    result = permutations(n-1)
    for i in range(1, n):
        result += (-1) ** i * combinations(n, i) * permutations(n - i - 1)
    result += (-1) ** n
    return result


# У кассы кинотеатра стоит m+k человек, m - рубли, k - полтинники. Билет стоит 50 копеек
# Ск-ми способами можно поставить очередь, что б не было задержек?
def task20(m, k):
    return permutations(k+1, m-1)


# У кассы кинотеатра стоит m+k человек, m - рубли, k - полтинники.
# В кассе лежит q полтинников. Билет стоит 50 копеек
# Ск-ми способами можно поставить очередь, что б не было задержек?
def task21(m, k, q):
    return permutations(k+q+1, m-q-1)


# m - 0, k - 1. Ск-ко существует последовательностей, для которых для любого i,
# кол-во 0 не больше чем 1 (кроме i = 1)
def task22(m, k):
    return permutations_with_repetitions(m, k) - 2 * permutations_with_repetitions(m-1, k)


# task 22, только m = k = n
def task23(n):
    return permutations_with_repetitions(n-1, n-1) - permutations_with_repetitions(n, n-2)


# Ск-ми способами можно построить 2*n человек разного роста, чтобы в каждой шеренге они стояли по росту
# и человек во второй шеренге был ниже стоящего перед ним
def task24(n):
    return combinations(2*n, n) // (n+1)


# Домино 28 костей. Ск-ко способов разделить на 4?
def task25():
    return permutations(28) / permutations(7) ** 4


# Двое ребят собрали n-ромашек, m-васильков, k-незабудок. Ск-ко способов разделить их?
def task26(n, m, k):
    return (n+1) * (m+1) * (k+1)


# n ребят собрали k яблок. Все яблоки одинаковы. Ск-ко способов разделить?
def task27(n, k):
    return permutations_with_repetitions(n-1, k)


# Есть n - флагов, k-матч. Ск-ми сп-ми их расставить, некоторые матчи могут быть пустые
def task28(n, k):
    return permutations(n) * combinations(n+k-1, k-1)


# Полное число сигналов, которые можно передеать с помощью n флагов и k матч.
def task29(n, k):
    result = 1
    for i in range(1, n+1):
        result += combinations(n, i) * placements(i + k - 1, i)
    return result

