def find_intersections(lists):
    all_elements = set()
    for l in lists:
        all_elements.update(l)

    elements = []

    for e in all_elements:

        count = 0

        for l in lists:
            if e in l:
                count += 1
        
        if count > 1:
            elements.append(e)
    
    return elements


if __name__ == '__main__':
    lists = []
    for _ in range(3):
        _ = input()
        numbers = set(map(int, input().split()))
        lists.append(numbers)

    intersection = find_intersections(lists)
    print(*map(str, intersection))
