def find_subsums(orcs):
    subsums = [0]

    for orc in orcs:
        subsums.append(subsums[-1] + orc)

    return subsums


def find_squads(orcs, forays):
    answers = []
    subsums = find_subsums(orcs)
    
    for foray in forays:

        left = 0
        right = len(orcs) - foray[0]

        while left <= right:
            middle = (left + right) // 2
            end_idx = middle + foray[0]

            s = subsums[end_idx] - subsums[middle]
            
            if s == foray[1]:
                answers.append(middle + 1)
                break
            elif s < foray[1]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            answers.append(-1)

    return answers


if __name__ == '__main__':
    _, m = list(map(int, input().split()))
    orcs = list(map(int, input().split()))
    forays = []

    for _ in range(m):
        forays.append(tuple(map(int, input().split())))
    
    answers = find_squads(orcs, forays)
    print("\n".join(map(str, answers)))
