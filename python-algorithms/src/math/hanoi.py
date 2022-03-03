def hanoi(disks):
    assert disks >= 0
    if disks <= 1:
        return disks
    return 2 * hanoi(disks-1) + 1
