def min_score_to_win(score1, current_score2, is_first_game_guest):
    total_score_team1 = score1[0] + current_score2[0]
    total_score_team2 = score1[1] + current_score2[1]
    diff = total_score_team2 - total_score_team1

    if diff < 0:
        return 0

    if diff == 0:

        if is_first_game_guest:

            if score1[0] > current_score2[1]:
                return 0

            return 1

        # Currently playing guest
        if current_score2[0] > score1[1]:
            return 0
        return 1

    # Team 1 have less points

    if is_first_game_guest:
        # Team 1 won first game as guest
        if score1[0] > current_score2[1]:
            return diff
        return diff + 1

    # currently play as guest
    if diff + current_score2[0] > score1[1]:
        return diff
    return diff + 1


if __name__ == '__main__':
    score1 = list(map(int, input().split(':')))
    current_score2 = list(map(int, input().split(':')))
    is_first_game_guest = int(input()) == 2
    n = min_score_to_win(score1, current_score2, is_first_game_guest)
    print(n)
