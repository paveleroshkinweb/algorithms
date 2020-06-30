def find_last_date(exams):
    dates = []
    sorted_exams = sorted(exams, key=lambda ex: (ex[0], ex[1]))
    prev = 0
    for act_date, poss_date in sorted_exams:
        if poss_date >= prev:
            dates.append(poss_date)
            prev = poss_date
        else:
            dates.append(act_date)
            prev = act_date
    return dates[-1]


if __name__ == '__main__':
    exams = [[int(e) for e in input().split()] for _ in range(int(input()))]
    print(find_last_date(exams))