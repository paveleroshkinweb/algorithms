def find_teams(rangers_experience):
    sorted_experience = sorted(rangers_experience)
    count_teams = 0
    used = 0
    for exp in sorted_experience:
        used += 1
        if used == exp:
            count_teams += 1
            used = 0
    return count_teams

if __name__ == '__main__':
    experiences = []
    for _ in range(int(input())):
        _ = input()
        experiences.append([int(s) for s in input().split()])
    for e in experiences:
        print(find_teams(e))
