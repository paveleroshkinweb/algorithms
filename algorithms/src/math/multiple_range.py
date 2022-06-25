# Task: given n numbers [a1, a2, .... ,an] How many numbers in range [1, r] which multiple by any of ai


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


def lcm(a, b):
    return (a*b) // gcd(a, b)

# Time complexity: O(n*r)
def multiple_range(numbers, r):
    count = 0
    for i in range(1, r+1):
        for number in numbers:
            if i % number == 0:
                count += 1
                break
    return count
