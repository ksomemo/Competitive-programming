def count_jump(pos_list, inv_pos_list, L):
    jump_count = 0
    if len(pos_list) == 0:
        for i, p in enumerate(inv_pos_list):
            jump_count += p - i - 1
            print("jump cnt zero:", jump_count)
    elif len(inv_pos_list) == 0:
        for i, p in enumerate(pos_list):
            jump_count += L - p - i
            print("jump cnt zero:", jump_count)
    else:
        if len(pos_list) > len(inv_pos_list):
            for i, p in enumerate(pos_list):
                jump_count += inv_pos_list[0] - p - i - 1
                print("jump cnt:", jump_count)
        else:
            for i, p in enumerate(inv_pos_list):
                jump_count += p - pos_list[-1] - i - 1
                print("jump cnt inv:", jump_count)
    return jump_count

def solve(rabbits, L):
    # 最初は右向き
    jump_count = 0
    bef_d = 'R'
    pos_list = []
    inv_pos_list = []

    for n_pos, n_d in rabbits:
        print("before direction:", bef_d)
        print("now direction:", n_d)
        print("now pos:", n_pos)
        print("pos:", pos_list)
        print("pos inv:", inv_pos_list)
        print("jump cnt:", jump_count)

        # 背中合わせになったら、前の区間のJUMP回数を求める
        if bef_d == 'L' and n_d == 'R':
            jump_count += count_jump(pos_list, inv_pos_list, L)

            pos_list = []
            inv_pos_list = []

        # うさぎを集める
        if n_d == 'R':
            pos_list.append(n_pos)
        else:
            inv_pos_list.append(n_pos)
        # 前回の方向を保持
        bef_d = n_d
        print("")

    print("before direction:", bef_d)
    print("pos:", pos_list)
    print("pos inv:", inv_pos_list)
    print("jump cnt:", jump_count)
    # 右向きの最大と、左向きの最小の位置の差を見る
    #　それぞれの方向別にjumpできる奥の位置がわかる
    # 奥の位置とうさぎの位置との差分
    jump_count += count_jump(pos_list, inv_pos_list, L)

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
