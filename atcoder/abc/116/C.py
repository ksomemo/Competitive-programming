def main():
    N = int(input())
    *h, = map(int, input().split())

    ans = f(N, h)
    print(ans)


def f(N, h):
    """
    1 <= N <= 100
    0 <= hi <= 100
    整数 l,r を指定する。
    l ≦ x ≦ r を満たすすべての xに対して、花 xの高さを 1高くする。
    条件を満たすための最小の「水やり」操作の回数を求めてください。

    広い範囲の花を高くしたいが、hk を超えてはいけない
    愚直にやる
        各kについてh回水をやる: sum(h)

    広範囲にやりすぎて回数が増えることはあるのか？
    間が多い
        0: 1 1 2 2 1
        1: 0 0 1 1 0
        2: 0 0 0 0 0
    端が多い
        0: 2 2 1 1 2
        1: 1 1 1 1 2, 1 1 0 0 1
        2: 0 0 0 0 1, 0 0 0 0 1
        3: 0 0 0 0 0
    跨ぐ
        0: 1 2 2 1 2
        1: 0 1 1 1 2, 0 1 1 0 1
        2: 0 0 0 0 1, 0 0 0 0 1
        3: 0 0 0 0 0

    愚直にやるでいいのでは
    """
    h = h[:]
    ans = 0
    while True:
        water = False
        for k in range(N):
            if h[k] == 0:
                if water:
                    break
            else:
                h[k] -= 1
                water = True

        if not water:
            break
        ans += 1

    return ans


if __name__ == '__main__':
    main()
