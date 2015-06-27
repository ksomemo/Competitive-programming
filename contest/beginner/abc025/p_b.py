import functools


def solve(move_num, move_min, move_max, patterns):
    west_d = [distance for direction, distance in patterns if direction == "West"]
    east_d = [distance for direction, distance in patterns if direction == "East"]

    f = functools.partial(move_d, move_min=move_min, move_max=move_max)
    pos = sum(map(f, east_d)) - sum(map(f, west_d))

    initial_position = 0
    if pos == initial_position:
        return "0"
    elif pos < initial_position:
        return "West {0}".format(abs(pos))

def move_d(distance, move_min, move_max):
    if distance > move_max:
        return move_max
    elif distance < move_min:
        return move_min
    return distance
