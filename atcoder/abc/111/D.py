from collections import Counter


def main():
    """
    ロボットアーム

    腕、関節
        arm_1, arm_2,...,arm_m
    k_0,  k_1,   k_2,...,  k_m

    k_i-1, arm_i, k_i
    arm_i_length: d_i

    mode: L, R, D, U

        (x0, y0) = (0, 0)
        L: (x_i, y_i) = (x_i-1 - d_i, y_i-1)
        R: (x_i, y_i) = (x_i-1 + d_i, y_i-1)
        U: (x_i, y_i) = (x_i-1,       y_i-1 - d_i)
        D: (x_i, y_i) = (x_i-1,       y_i-1 + d_i)

    input:
            1 <= N  <= 10^3
        -10^9 <= Xi <= 10^9
        -10^9 <= Yi <= 10^9

    output:
        NG: -1
        OK:

        m
        d1 d2 ... dm
        w1
        w2
        ...
        wN

        1 <= m   <= 40
        1 <= d_i <= 10^12
        w_i: {L, R, U, D}, w_i_lenght = m

    動かし方の例は、入力例1参照
    """
    N = int(input())
    X, Y = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    m, d, w = part_300(N, X, Y)
    # m, d, w = ex1(N, X, Y)
    print(m)
    print(*d)
    print(*w, sep="\n")


def ex1(N, X, Y):
    m = 2
    d = [1, 2]
    w = ["RL", "UU", "DR"]
    return m, d, w


def part_300(N, X, Y):
    """
    1つ1つのクエリに対する操作は独立
    ただし、使うパラメータm, d は共通

    部分点は以下の制約
       -10 <= i <= 10
       -10 <= i <= 10

    探索範囲
        20 * 20
        この範囲においてm<=40で到達するためのd
    d=1のとき|X|+|Y|の偶奇
        揃っている場合、mは最大に合わせる、余っているときはRLのように移動なしにできる    
        揃っていない場合, d=1では不可能？
        2と1およびLR,UDを駆使して-1を再現して偶奇を揃える?
            無理っぽい: 奇数しか作れない
    """
    dists = []
    for x, y in zip(X, Y):
        dist = abs(x) + abs(y)
        dists.append(dist)

    mod = list(map(lambda x: x % 2, dists))
    if len(set(mod)) == 1:
        m = max(dists)
        d = [1] * m
        w = []
        for x, y, dist in zip(X, Y, dists):
            x_dir = "R" if x > 0 else "L"
            y_dir = "U" if y > 0 else "U"

            _w = x_dir * abs(x) + y_dir * abs(y)
            rest = dist - len(x)
            if rest > 0:
                _w += "LR" * (rest // 2)
            w.append(_w)
    else:
        pass

    return m, d, w


def editorial(N, X, Y):
    pass


if __name__ == '__main__':
    main()
