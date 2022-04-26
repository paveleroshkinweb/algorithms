def random_teams(n_peoples, n_teams):
    if n_peoples == n_teams:
        return '0 0'
    n_max = n_peoples - n_teams + 1
    max_friends = n_max * (n_max - 1) // 2
    min_teams_1 = n_peoples // n_teams
    min_teams_2 = min_teams_1 + 1
    number_teams_2 = n_peoples % n_teams
    number_teams_1 = n_teams - number_teams_2
    min_friends = (
        number_teams_1 * min_teams_1 * (min_teams_1 - 1) // 2 +
        number_teams_2 * min_teams_2 * (min_teams_2 - 1) // 2
    )
    return f'{min_friends} {max_friends}'


if __name__ == '__main__':
    data = [int(e) for e in input().split()]
    print(random_teams(*data))
