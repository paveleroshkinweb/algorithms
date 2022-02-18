def diskStacking(disks):
    sorted_disks = sorted(disks, key=lambda disk: (disk[0], disk[1], disk[2]))
    groups = []
    heights = []
    for disk in sorted_disks:
        found = False
        for idx, group in enumerate(groups):
            last_disk = group[-1]
            if can_stack(last_disk, disk):
                group.append(disk)
                heights[idx] += disk[2]
                found = True
        if not found:
            groups.append([disk])
            heights.append(disk[2])
    index_max = max(range(len(heights)), key=heights.__getitem__)
    return groups[index_max]


def can_stack(disk1, disk2):
    return all(disk1[i] < disk2[i] for i in range(len(disk1)))