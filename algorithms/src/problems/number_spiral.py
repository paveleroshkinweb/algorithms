def find_number(x, y):
    squre_size = max(x, y)
    max_square = squre_size ** 2
    min_square = (squre_size - 1) ** 2 + 1
 
    isIncreasingSquare = max_square & 1 
    
    if x > y:
        
        if isIncreasingSquare:
            return max_square - y + 1
        
        return min_square + y - 1
 
    if isIncreasingSquare:
        return min_square + x - 1
    return max_square - x + 1
 
 
if __name__ == '__main__':
    all_coordinates = []
    for _ in range(int(input())):
        coordinate = reversed(list(map(int, input().split())))
        all_coordinates.append(coordinate)
 
    numbers = (find_number(x, y) for x, y in all_coordinates)
    print("\n".join(map(str, numbers)))
