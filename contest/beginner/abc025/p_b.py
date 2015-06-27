import functools


def solve(move_min, move_max, patterns):
    west_d = [distance for direction, distance in patterns if direction == "West"]
    east_d = [distance for direction, distance in patterns if direction == "East"]

    f = functools.partial(move_d, move_min=move_min, move_max=move_max)
    pos = sum(map(f, east_d)) - sum(map(f, west_d))

    initial_position = 0
    if pos == initial_position:
        return "0"
    elif pos < initial_position:
        return "West {0}".format(abs(pos))
    else:
        return "East {0}".format(pos)

def move_d(distance, move_min, move_max):
    if distance > move_max:
        return move_max
    elif distance < move_min:
        return move_min
    return distance

# templates
def input_str():
        return input().strip('\n')

def input_int():
        return int(input_str())

def input_str_l(sep=None):
        return input_str().split(sep)

def input_int_l(sep=None):
        return map(int, input_str_l(sep))

if __name__ == "__main__":
    move_num, move_min, move_max = input_int_l()
    patterns = []
    for _ in range(move_num):
        direction, distance = input_str_l()
        patterns.append((direction, int(distance)))

    result = solve(move_min, move_max, patterns)
    print(result)
