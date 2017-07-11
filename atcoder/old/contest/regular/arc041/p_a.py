def solve(front, back, turn):
    if back >= turn:
        return front + turn

    # 裏返し切れなかった数を元に戻す
    return front + back - (turn - back)

# util
def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

if __name__ == '__main__':
    front, back = input_int_l()
    turn = input_int()
    print(solve(front, back, turn))
