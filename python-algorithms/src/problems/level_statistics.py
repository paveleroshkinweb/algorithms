def is_valid_sequence(sequence):
    prev_attempts = prev_successful_attempts = 0
    for attempts, successful_attempts in sequence:
        if (successful_attempts > attempts
                or attempts < prev_attempts
                or successful_attempts < prev_successful_attempts
                or attempts - prev_attempts < successful_attempts - prev_successful_attempts):
            return "NO"
        prev_attempts, prev_successful_attempts = attempts, successful_attempts
    return "YES"


if __name__ == '__main__':
    sequence_of_attempts = []
    for _ in range(int(input())):
        attempts = []
        for _ in range(int(input())):
            attempts.append([int(s) for s in input().split()])
        sequence_of_attempts.append(attempts)
    results = [is_valid_sequence(s) for s in sequence_of_attempts]
    print('\n'.join(results))