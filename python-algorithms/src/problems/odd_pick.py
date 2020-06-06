def possible_odd_sum(data):
    x, array = data
    even_number = len([number for number in array if number % 2 == 0])
    odd_number = len(array) - even_number
    need_odd = 1 if even_number >= x else x - even_number
    if need_odd % 2 == 0:
        need_odd = min(x, need_odd + 1)
    return "YES" if odd_number >= need_odd and need_odd % 2 != 0 else "NO"


if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        x = int(input().split()[1])
        array = [int(s) for s in input().split()]
        data.append((x, array))
    for d in data:
        print(possible_odd_sum(d))