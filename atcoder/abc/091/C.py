from collections import deque


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
        tuple(map(int, input().split()))
        for _ in range(N)
    ]
    cd = [
        tuple(map(int, input().split()))
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

    左下にある赤は価値が高い
    x座標の小さい青から始めているので, 赤x座標は青xより小さいものが対象
    y座標が高いものを選ぶのは
    選定中の赤座標と次の青と比較した時,
        次の青は今の青よりxは大きい
        つまり今y選定している赤のxより必ず大きいためどのx座標であるかは気にならない
        yが小さいものとペアにしたとき,とらなかったmax_yが次の青yより大きい可能性があるため
    """
    cd = deque(sorted(cd))

    used = [False] * N
    ans = 0
    while cd:
        c, d = cd.popleft()
        ai, ay = None, -1
        for i, (a, b) in enumerate(ab):
            if used[i]:
                continue
            if a < c and b < d:
                if b > ay:
                    ai, ay = i, b

        if ai is not None:
            # sorted abに対して見つかった瞬間にペアにしていたがy判断をする
            used[ai] = True
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
