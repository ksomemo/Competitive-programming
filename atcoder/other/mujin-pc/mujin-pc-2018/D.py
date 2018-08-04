def main():
    N, M = map(int, input().split())

    ans = f(N, M)
    print(ans)


def rev(x):
    return int(str(x)[::-1])


def test_rev():
    x_ans = [
        (123, 321),
        (90, 9),
        (5, 5)
    ]
    for x, ans in x_ans:
        assert rev(x) == ans


def f(N, M):
    """
    1 <= N, M <= 999

    1: x,y のいずれかが 0なら、終了する
    2: x < y なら
        x を rev(x) で、
        そうでないなら y を rev(y) で置き換える。
    3: 上の操作後、x<y となっていれば 
        y を y−xで、
        そうでなければ x を x−yで置き換える。

    """
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            s = set()
            # print(i, j)
            x, y = i, j
            while True:
                # print("\t", x, y)
                # 無限ループ判定
                if (x, y) in s:
                    ans += 1
                    break

                s.add((x, y))
                if x == 0 or y == 0:
                    break

                if x < y:
                    x = rev(x)
                else:
                    y = rev(y)

                if x < y:
                    y -= x
                else:
                    x -= y

    return ans


if __name__ == '__main__':
    main()
