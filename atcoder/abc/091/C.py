def main():
    """
    ab: red
    cd: blue

    仲良しペア: 最大で何個
        赤い点の x座標が青い点の x座標より小さい
        赤い点の y座標も青い点の y座標より小さい
        1つの点が複数のペアに所属することはできません。
    """
    N = int(input())

    ab = [
        tuple(map(int,input().split()))
        for _ in range(N)
    ]
    cd = [
        tuple(map(int,input().split()))
        for _ in range(N)
    ]

    f(N, ab, cd)

def f(N, ab, cd):
    """
    sortしてみたけどダメだった
        左下にある青
        右上にある赤
    N=100
    全ペア作ってみる: TLE
        ab/cdの全並べ方の組合せ
            ab permutation N!
            cd permutation N!
            N! * N!

    b1-a1
    b1-a2
    """
    from collections import deque
    ab = sorted(ab, reverse=True)
    cd = deque(sorted(cd))

    used = [False] * N
    ans = 0
    while cd:
        c, d = cd.popleft()
        print((c, d), "----------")
        for i, (a, b) in enumerate(ab):
            print(i, (a, b))
            if used[i]:
                continue
            if a < c and b < d:
                ans += 1
                used[i] = True
                break

    print(ans)


if __name__ == '__main__':
    main()
