import argparse
import json


# Сложность алгоритма O(n)
# Задача решалась методами динамического программирования
# Идея: для каждого элемента найти лучшую подпоследовательность
# включающую данный элемент и итеративно наращивать решение
# Общее решение задачи гарантированно находится среди последних 2 элементов в solutions
# Пример запуска программы: python solution.py '[0, 1, 1, 3, 1, 1, 5]'

def find_max_vaccine(universes):
    if len(universes) <= 2:
        return max(universes)
    solutions = {-1: 0, 0: universes[0], 1: universes[1]}
    for i in range(2, len(universes)):
        solutions[i] = universes[i] + max(solutions[i-2], solutions[i-3])
    return max(solutions[len(universes)-1], solutions[len(universes)-2])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('universes')
    args = parser.parse_args()
    universes = [int(universe) for universe in json.loads(args.universes)]
    print(find_max_vaccine(universes))
