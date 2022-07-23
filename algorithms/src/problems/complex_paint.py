def complex_paint(numbers):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    last_color = 0
    number_colors = []
    colors = {}
    for number in numbers:
        for prime in primes:
            if number % prime == 0:
                if prime not in colors:
                  last_color += 1
                  colors[prime] = last_color
                number_colors.append(colors[prime])
                break
    return len(colors), number_colors


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        numbers = list(map(int, input().split(' ')))
        colors, paint = complex_paint(numbers)
        results.append(str(colors))
        results.append(" ".join(map(str, paint)))
    print("\n".join(results))
