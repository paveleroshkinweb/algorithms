def get_min_obstacle(obstacle_type, obstacle1, obstacle2):
    if obstacle_type in ['left-horizontal', 'left-top-diagonal', 'left-bot-diagonal'] and obstacle1[1] > obstacle2[1]:
        return obstacle1
    elif obstacle_type in ['right-horizontal', 'right-top-diagonal', 'right-bot-diagonal'] \
            and obstacle1[1] < obstacle2[1]:
        return obstacle1
    elif obstacle_type == 'top-vertical' and obstacle1[0] < obstacle2[0]:
        return obstacle1
    elif obstacle_type == 'bot-vertical' and obstacle1[0] > obstacle2[0]:
        return obstacle1
    return obstacle2


def get_diagonal_top_points(n, r_q, c_q):
    left_top_point = get_left_diagonal_top_point(n, r_q, c_q)
    right_top_point = get_right_diagonal_top_point(n, r_q, c_q)
    return left_top_point, right_top_point


def get_left_diagonal_top_point(n, r_q, c_q):
    left_top_delta = min(n - r_q, c_q - 1)
    left_top_point = (r_q + left_top_delta, c_q - left_top_delta)
    return left_top_point


def get_right_diagonal_top_point(n, r_q, c_q):
    right_top_delta = min(n - c_q, n - r_q)
    right_top_point = (r_q + right_top_delta, c_q + right_top_delta)
    return right_top_point


def get_diagonal_bot_points(n, r_q, c_q):
    left_bot_point = get_left_diagonal_bot_point(n, r_q, c_q)
    right_bot_point = get_right_diagonal_bot_point(n, r_q, c_q)
    return left_bot_point, right_bot_point


def get_left_diagonal_bot_point(n, r_q, c_q):
    left_bot_delta = min(r_q - 1, c_q - 1)
    left_bot_point = (r_q - left_bot_delta, c_q - left_bot_delta)
    return left_bot_point


def get_right_diagonal_bot_point(n, r_q, c_q):
    right_bot_delta = min(r_q - 1, n - c_q)
    right_bot_point = (r_q - right_bot_delta, c_q + right_bot_delta)
    return right_bot_point


def check_if_point_on_the_line(point1, point2, point3):
    return (point2[1] - point1[1])/((point2[0] - point1[0]) or 1) == (point3[1] - point1[1])/((point3[0] - point1[0]) or 1)


def is_horizontal_obstacle(obstacle, r_q, c_q):
    return obstacle[0] == r_q


def define_horizontal_obstacle(n, obstacle, r_q, c_q):
    return 'left-horizontal' if obstacle[1] < c_q else 'right-horizontal'


def is_vertical_obstacle(obstacle, r_q, c_q):
    return obstacle[1] == c_q


def define_vertical_obstacle(n, obstacle, r_q, c_q):
    return 'bot-vertical' if obstacle[0] < r_q else 'top-vertical'


def is_top_diagonal_obstacle(obstacle, r_q, c_q):
    return obstacle[0] > r_q


def define_top_diagonal_obstacle(n, obstacle, r_q, c_q):
    queen_coordinates = (r_q, c_q)
    left_top_point, right_top_point = get_diagonal_top_points(n, r_q, c_q)
    if check_if_point_on_the_line(queen_coordinates, left_top_point, obstacle):
        return 'left-top-diagonal'
    elif check_if_point_on_the_line(queen_coordinates, right_top_point, obstacle):
        return 'right-top-diagonal'
    return None


def is_bot_diagonal_obstacle(obstacle, r_q, c_q):
    return obstacle[0] < r_q


def define_bot_diagonal_obstacle(n, obstacle, r_q, c_q):
    queen_coordinates = (r_q, c_q)
    left_bot_point, right_bot_point = get_diagonal_bot_points(n, r_q, c_q)
    if check_if_point_on_the_line(queen_coordinates, left_bot_point, obstacle):
        return 'left-bot-diagonal'
    elif check_if_point_on_the_line(queen_coordinates, right_bot_point, obstacle):
        return 'right-bot-diagonal'
    return None


def queens_attack(n, r_q, c_q, obstacles):
    nearest_obstacles = find_nearest_obstacles(n, r_q, c_q, obstacles)
    return count_targets(n, r_q, c_q, nearest_obstacles)


def find_nearest_obstacles(n, r_q, c_q, obstacles):
    nearest_obstacles_map = {}
    for obstacle in obstacles:
        obstacle_type = get_obstacle_type(n, r_q, c_q, obstacle)
        if obstacle_type is not None:
            if nearest_obstacles_map.get(obstacle_type) is None:
                nearest_obstacles_map[obstacle_type] = obstacle
            else:
                nearest_obstacles_map[obstacle_type] = get_min_obstacle(obstacle_type,
                                                                        obstacle,
                                                                        nearest_obstacles_map[obstacle_type])
    return nearest_obstacles_map


def get_obstacle_type(n, r_q, c_q, obstacle):
    obstacle_type_detection = {
        'horizontal': {
            'check': is_horizontal_obstacle,
            'define': define_horizontal_obstacle
        },
        'vertical': {
            'check': is_vertical_obstacle,
            'define': define_vertical_obstacle
        },
        'top-diagonal': {
            'check': is_top_diagonal_obstacle,
            'define': define_top_diagonal_obstacle
        },
        'bot-diagonal': {
            'check': is_bot_diagonal_obstacle,
            'define': define_bot_diagonal_obstacle
        }
    }
    for common_type in obstacle_type_detection:
        handler = obstacle_type_detection[common_type]
        if handler['check'](obstacle, r_q, c_q):
            return handler['define'](n, obstacle, r_q, c_q)
    return None


def count_targets(n, r_q, c_q, nearest_obstacles):
    all_obstacle_types = [
        'left-horizontal',
        'left-top-diagonal',
        'left-bot-diagonal',
        'right-horizontal',
        'right-top-diagonal',
        'right-bot-diagonal',
        'top-vertical',
        'bot-vertical'
    ]
    targets = 0
    queen_coordinates = (r_q, c_q)
    for obstacle_type in all_obstacle_types:
        targets += count_targets_by_type(n, obstacle_type, queen_coordinates, nearest_obstacles.get(obstacle_type))
    return targets


def count_targets_by_type(n, obstacle_type, queen_coordinates, nearest_obstacle):
    handlers = {
        'left-horizontal': {
            'without': lambda n, queen_coordinates: queen_coordinates[1] - 1,
            'with': lambda n, queen_coordinates, nearest_obstacle: queen_coordinates[1] - nearest_obstacle[1] - 1
        },
        'right-horizontal': {
            'without': lambda n, queen_coordinates: n - queen_coordinates[1],
            'with': lambda n, queen_coordinates, nearest_obstacle: nearest_obstacle[1] - queen_coordinates[1] - 1
        },
        'top-vertical': {
            'without': lambda n, queen_coordinates: n - queen_coordinates[0],
            'with': lambda n, queen_coordinates, nearest_obstacle: nearest_obstacle[0] - queen_coordinates[0] - 1
        },
        'bot-vertical': {
            'without': lambda n, queen_coordinates: queen_coordinates[0] - 1,
            'with': lambda n, queen_coordinates, nearest_obstacle: queen_coordinates[0] - nearest_obstacle[0] - 1
        },
        'left-top-diagonal': {
            'without': lambda n, queen_coordinates: queen_coordinates[1] - get_left_diagonal_top_point(n, queen_coordinates[0], queen_coordinates[1])[1],
            'with': lambda n, queen_coordinates, nearest_obstacle: queen_coordinates[1] - nearest_obstacle[1] - 1
        },
        'right-top-diagonal': {
            'without': lambda n, queen_coordinates: get_right_diagonal_top_point(n, queen_coordinates[0], queen_coordinates[1])[1] - queen_coordinates[1],
            'with': lambda n, queen_coordinates, nearest_obstacle: nearest_obstacle[1] - queen_coordinates[1] - 1
        },
        'left-bot-diagonal': {
            'without': lambda n, queen_coordinates: queen_coordinates[1] - get_left_diagonal_bot_point(n, queen_coordinates[0], queen_coordinates[1])[1],
            'with': lambda n, queen_coordinates, nearest_obstacle: queen_coordinates[1] - nearest_obstacle[1] - 1
        },
        'right-bot-diagonal': {
            'without': lambda n, queen_coordinates: get_right_diagonal_bot_point(n, queen_coordinates[0], queen_coordinates[1])[1] - queen_coordinates[1],
            'with': lambda n, queen_coordinates, nearest_obstacle: nearest_obstacle[1] - queen_coordinates[1] - 1
        }
    }
    handler = handlers[obstacle_type]
    return handler['without'](n, queen_coordinates) if nearest_obstacle is None else handler['with'](n, queen_coordinates, nearest_obstacle)