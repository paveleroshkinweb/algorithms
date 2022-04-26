def organizingContainers(container):
    containers_capacity = get_containers_capacity(container)
    balls_count = get_balls_count(container)
    return 'Possible' if containers_capacity == balls_count else 'Impossible'


def get_containers_capacity(containers):
    containers_capacity = {}
    for container in containers:
        capacity = sum(container)
        containers_capacity[capacity] = (containers_capacity.get(capacity) or 0) + 1
    return containers_capacity


def get_balls_count(containers):
    balls_count = {}
    for i in range(len(containers)):
        cur_sum = 0
        for j in range(len(containers)):
            cur_sum += containers[j][i]
        balls_count[cur_sum] = (balls_count.get(cur_sum) or 0) + 1
    return balls_count
