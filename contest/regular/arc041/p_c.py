def count_jump(right_list, left_list, L):
    jump_count = 0
    if len(right_list) == 0:
        for i, p in enumerate(left_list):
            jump_count += p - i - 1
    elif len(left_list) == 0:
        for i, p in enumerate(right_list):
            jump_count += L - p - i
    else:
        # 各向きのグループの間隔を詰める
        for i, p in enumerate(right_list):
            jump_count += right_list[-1] -p - i
        for i, p in enumerate(left_list):
            jump_count += p - left_list[0] - i

        # グループ先頭同士の間を片方のグループを進めて詰める
        head_diff = left_list[0] - right_list[-1] - 1
        max_cnt = max(len(right_list), len(left_list))
        jump_count += head_diff * max_cnt

    return jump_count

def solve(rabbits, L):
    # 最初は右向き
    jump_count = 0
    bef_d = 'R'
    right_list = []
    left_list = []

    for n_pos, n_d in rabbits:
        # 背中合わせになったら、向き合っているグループのJUMP回数を求める
        if bef_d == 'L' and n_d == 'R':
            jump_count += count_jump(right_list, left_list, L)

            right_list = []
            left_list = []

        # うさぎを集める
        if n_d == 'R':
            right_list.append(n_pos)
        else:
            left_list.append(n_pos)
        # 前回の方向を保持
        bef_d = n_d

    jump_count += count_jump(right_list, left_list, L)

    return jump_count

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
    N, L = input_int_l()
    rabbits = []
    for _ in range(N):
        pos, direction = input_str_l()
        rabbits.append((int(pos), direction))
    result = solve(rabbits, L)
    print(result)
