def count_sweets(sweets):
    players = {
        # pointer, diff, prev_sweets, total
        False: [0, 1, 0, 0],
        True: [len(sweets) - 1, -1, 0, 0]
    }
    steps = 0
    current_player = False
    while players[False][0] <= players[True][0]:
        steps += 1
        need_to_eat = players[not current_player][2]
        eat = 0
        while need_to_eat >= eat and players[False][0] <= players[True][0]:
            eat += sweets[players[current_player][0]]
            players[current_player][0] += players[current_player][1]
        players[current_player][3] += eat
        players[current_player][2] = eat
        current_player = not current_player
    return steps, players[False][3], players[True][3]


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        sweets = [int(e) for e in input().split(' ')]
        steps, alice_sweets, bob_sweets = count_sweets(sweets)
        results.append(f'{steps} {alice_sweets} {bob_sweets}')
    print("\n".join(results))