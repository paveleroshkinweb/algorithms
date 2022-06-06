def calculate_queries(array, queries):
    array_sum = sum(array)
    prefixes = [array_sum]
    sub_sum = array[0]
    for i in range(1, len(array)):
        prefixes.append(array_sum - sub_sum)
        sub_sum += array[i]
    prefixes.append(0)
    results = []
    for start, end in queries:
        result = prefixes[start] - prefixes[end+1]
        results.append(str(result))
    return results


if __name__ == '__main__':
    queries_number = int(input().split(' ')[1])
    array = [int(e) for e in input().split(' ')]
    queries = []
    for _ in range(queries_number):
        query = [int(e) - 1 for e in input().split(' ')]
        queries.append(query)
    print("\n".join(calculate_queries(array, queries)))
