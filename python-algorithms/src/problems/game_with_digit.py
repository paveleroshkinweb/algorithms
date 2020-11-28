import math


def is_prime_odd(n):
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_winner(n):
    players = {
        0: 'Ashishgup',
        1: 'FastestFinger'
    }
    first_player_lose = n == 1
    if n > 2 and n % 2 == 0:
        if n & (n - 1) == 0:
            first_player_lose = 1
        elif n % 4 != 0 and is_prime_odd(n // 2):
            first_player_lose = 1
    return players[first_player_lose]


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        results.append(get_winner(int(input())))
    print('\n'.join(results))