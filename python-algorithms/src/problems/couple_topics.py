def get_diff(teacher_marks, student_marks):
    return sorted([t_mark - s_mark
                   for t_mark, s_mark
                   in zip(teacher_marks, student_marks)])


def binary_search(arr, i, el):
    left = i
    right = len(arr) - 1
    solution = -1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] + el > 0:
            solution = middle
            right = middle - 1
        else:
            left = middle + 1
    return solution


def get_couple_topics(teacher_marks, student_marks):
    diff = get_diff(teacher_marks, student_marks)
    couple_topics = 0
    for i in range(len(diff)):
        current_couples = binary_search(diff, i+1, diff[i])
        if current_couples != -1:
            couple_topics += len(diff) - current_couples
    return couple_topics


def get_arr():
    arr = input().split(' ')
    return [int(el) for el in arr]


if __name__ == '__main__':
    _ = input()
    teacher_marks, student_marks = get_arr(), get_arr()
    print(get_couple_topics(teacher_marks, student_marks))
