def main():
    N, H = map(int, input().split())
    ab = [
        [i] + list(map(int, input().split()))
        for i in range(N)
    ]

    # solve(N, H, ab)
    editorial(H, ab)


def editorial(H, ab):
    """
    max_a より大きいbを使う方針はOK
    max_a を持ち max_aより大きいbを持つ刀をどうするか？

    基本は合っていた
    投げた後のことを考えていたが
    投げるのは倒すときでよいので、それまでは切り続ける
    というのが解説の投げた後も使って良いということ
        b ... b + (a_max ... a_max + b_last)
        b ... b + (b_last + a_max ... a_max)
    """
    sorted_a = sorted(ab, key=lambda x: x[1], reverse=True)
    sorted_b = sorted(ab, key=lambda x: x[2], reverse=True)
    max_a = sorted_a[0][1]

    ans = 0
    for _, _, b in sorted_b:
        if max_a > b:
            break

        H -= b
        ans += 1
        if H <= 0:
            print(ans)
            return

    ans += (H + max_a - 1) // max_a
    print(ans)


def solve(N, H, ab):
    """ひどい…
    """
    from collections import Counter

    throwed = [False] * N
    n_throwed = 0
    sorted_a = sorted(ab, key=lambda x: x[1], reverse=True)
    sorted_b = sorted(ab, key=lambda x: x[2], reverse=True)

    print(sorted_a)
    print(sorted_b)

    max_b_i, max_a_i = 0, 0
    min_b_i, min_a_i = -1, -1
    a_c = Counter(a for i, a, b in ab)

    min_a = sorted_a[-1][1]
    min_b = sorted_b[-1][2]
    max_a = sorted_a[0][1]
    max_b = sorted_b[0][2]

    ans = 0
    n = 0
    while H > 0:
        n += 1
        print(n, H, (min_a, max_a, min_b, max_b),
              (max_b_i, max_a_i, min_b_i, min_a_i), throwed)
        if min_a >= max_b:
            # b_minよりa_maxのほうがダメージ強い場合、それで倒せば良い
            print("a")
            ans += (H + max_a - 1) // max_a
            break

        if max_b >= H:
            # bで倒せるなら終わり
            print("b")
            ans += 1
            break

        if max_a < min_b:
            # TODO: すべて投げたほうがダメージ強いとき
            # 最大Aを残して投げればよさそう?
            # あとはAで対処、またはBを投げて終了
            for k in range(max_b_i, N):
                # i, a, b -= sorted_b[i]
                if i == max_a_i:
                    continue
                H -= b
                throwed[i] = True
                ans += 1
                if H <= 0:
                    break
            max_b_i = max_a_i

        # 次に使うものを決める
        if max_a_i != max_b_i or a_c[max_a] >= 2:
            # aは今のbのaか？
            # そうでないなら、bを使う（bを投げてもaに影響がない）
            # そうであっても他のaと値が同じであれば問題ない
            print("c")
            th_idx = sorted_b[max_b_i][0]
            throwed[th_idx] = True
            n_throwed += 1
            H -= max_b
            max_b_i += 1
            max_b = sorted_b[max_b_i][2]
            ans += 1
            a_c[max_a] -= 1
            continue

        # aは今のbであり、他のaより大きい
        #   e.g.:
        #   b=10,a=9,a_2nd=5
        #   投げると次から5ずつ
        #   b_2nd?
        #     b_2nd: 9
        # 1.bを投げた後のシミュレーション
        # 2.aで切った後のシミュレーション
        #
        print("試行錯誤中")
        break

    print(ans)


if __name__ == "__main__":
    main()
