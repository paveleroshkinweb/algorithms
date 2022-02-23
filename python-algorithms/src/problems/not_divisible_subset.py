def nonDivisibleSubset(k, s):
    remain_groups = get_remain_groups(k, s)
    return find_longest_subset_length(remain_groups, k)


def get_remain_groups(k, s):
    remain_groups = {}
    for number in s:
        remain = number % k
        if (remain == 0 or 2*remain == k):
            remain_groups[remain] = 1
        else:
            remain_groups[remain] = (remain_groups.get(remain) or 0) + 1
    return remain_groups


def find_longest_subset_length(remain_groups, k):
    common_sum = sum(remain_groups.values())
    incompatible_groups = get_incompatible_groups(remain_groups, k)
    for incompatible_group in incompatible_groups:
        length1 = remain_groups[incompatible_group[0]]
        length2 = remain_groups[incompatible_group[1]]
        common_sum -= min(length1, length2)
    return common_sum


def get_incompatible_groups(remain_groups, k):
    incompatible_groups = []
    for remain in remain_groups:
        if remain <= k // 2:
            incompatible_remain = k - remain
            if incompatible_remain != remain and remain_groups.get(incompatible_remain) is not None:
                incompatible_groups.append((remain, incompatible_remain))
    return incompatible_groups