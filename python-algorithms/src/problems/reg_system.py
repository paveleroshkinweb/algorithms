def reg_system(data):
    db = {}
    counters = {}
    results = []
    for name in data:
        res = db.get(name, 'OK')
        if res == 'OK':
            counters[name] = 1
        else:
            counters[name] += 1
        db[name] = f'{name}{counters[name]}'
        results.append(res)
    return results


if __name__ == '__main__':
    data = [input() for _ in range(int(input()))]
    print('\n'.join(reg_system(data)), sep='')