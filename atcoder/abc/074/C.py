from itertools import product


def main():
    """
    1 ≦ A < B ≦ 30
    1 ≦ C < D ≦ 30
    1 ≦ E ≦ 100
    100A ≦ F ≦ 3000 より
       A,B: 30回まで
       C,D: 100回まで
    """
    A, B, C, D, E, F = map(int, input().split())

    ans_w = 0
    ans_s = 0
    for a, b, c in product(range(31),
                           range(31),
                           range(101)):
        for d in range(101):
            w = (100 * A * a) + (100 * B * b)
            s = C * c + D * d

            if w == 0 or (w + s) > F:
                break

            # Sugar: Water = E: 100
            if s * 100 == w * E:
                print(w + s, s)
                return

            # Sugar: Water > E: 100 なら溶け切らない
            # s/w > E/100
            if s * 100 > E * w:
                break

            # 以前の最大濃度との比較(基準の100, Eを置き換え)
            # s: w > a_w: a_s
            if (ans_w, ans_s) == (0, 0) or \
                    s * ans_w > ans_s * w:
                ans_w, ans_s = w, s

    print(ans_w + ans_s, ans_s)

if __name__ == '__main__':
    main()
