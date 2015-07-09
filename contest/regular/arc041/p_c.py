def solve(rabbits, L):
    # 最初は右向き
    jump_count = 0
    bef_d = 'R'
    pos_list = [0]
    inv_pos_list = []

    for n_pos, n_d in rabbits:
        print("before direction:", bef_d)
        print("now direction:", n_d)
        print("now pos:", n_pos)
        print("pos:", pos_list)
        print("pos inv:", inv_pos_list)
        print("jump cnt:", jump_count)

        if bef_d != n_d:
            if len(pos_list) > 0 and len(inv_pos_list) > 0:
                # 位置を両方向とも溜め込んでいたら
                # その時点でのJUMP回数を計算する
                diff = inv_pos_list[0] - pos_list[-1]
                print("diff:", diff)
                # 右向きの最大と、左向きの最小の位置の差を見る
                #　それぞれの方向別にjumpできる奥の位置がわかる
                # 奥の位置とうさぎの位置との差分
                if len(pos_list) == len(inv_pos_list):
                    for p in pos_list:
                        if p == 0: continue
                        jump_count += diff - 1
                        print("jump cnt eq:", jump_count)
                elif len(pos_list) > len(inv_pos_list):
                    for i, p in enumerate(pos_list):
                        diff = inv_pos_list[0] - p - i - 1
                        if p == 0: continue
                        jump_count += diff
                        print("jump cnt:", jump_count)
                else:
                    for i, p in enumerate(inv_pos_list):
                        diff = p - pos_list[-1] - 1 - i
                        jump_count += diff
                        print("jump cnt inv:", jump_count)

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

    if len(inv_pos_list) == 0:
        inv_pos_list.append(L+1)
    print("before direction:", bef_d)
    print("pos:", pos_list)
    print("pos inv:", inv_pos_list)
    print("jump cnt:", jump_count)
    diff = inv_pos_list[0] - pos_list[-1] - 1
    print("diff:", diff)
    # 右向きの最大と、左向きの最小の位置の差を見る
    #　それぞれの方向別にjumpできる奥の位置がわかる
    # 奥の位置とうさぎの位置との差分
    if len(pos_list) == len(inv_pos_list):
        for p in pos_list:
            if p == 0: continue
            jump_count += diff
            print("jump cnt eq:", jump_count)
    elif len(pos_list) > len(inv_pos_list):
        for i, p in enumerate(pos_list):
            diff = inv_pos_list[0] - p - i
            if p == 0: continue
            jump_count += diff
            print("jump cnt:", jump_count)
    else:
        for i, p in enumerate(inv_pos_list):
            # 間隔を求める(前のうさぎによって一番奥より１つ後ろにいくことになる)
            diff = p - pos_list[-1] - 1 - i
            jump_count += diff
            print("jump cnt inv:", jump_count)

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
