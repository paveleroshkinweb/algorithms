def getLowestCommonManager(topManager, reportOne, reportTwo):
    queue = [(None, topManager, 0)]
    parents = {}
    while queue:
        parent, node, level = queue.pop()
        parents[node] = (parent, level)
        for report in node.directReports:
            queue.append((node, report, level + 1))
    parent1, node1_level = parents[reportOne]
    parent2, node2_level = parents[reportTwo]

    node1 = parent1
    node2 = parent2
    while node1_level != node2_level:
        if node1_level > node2_level:
            node1 = parent1
            parent1, node1_level = parents[parent1]
        else:
            node2 = parent2
            parent2, node2_level = parents[parent2]
    if node1 == reportTwo:
        return reportTwo
    if node2 == reportOne:
        return reportOne
