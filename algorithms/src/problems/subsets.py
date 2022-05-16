def subsets(n):
    acc_subsets = [set()]

    def helper(k, subset):
        if k == n + 1:
            return subset
        subset.append(k)
        acc_subsets.append(set(subset))
        helper(k + 1, subset)
        subset.pop()
        helper(k + 1, subset)

    helper(1, [])
    return acc_subsets
