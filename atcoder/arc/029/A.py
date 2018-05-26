import sys


def main():
    N = int(input())
    ts = [int(input()) for _ in range(N)]

    search(N, ts)


def AC(N, ts):
    """
    時間がかからないものから、と思ったがWAは実装ミスっぽい
    diffとらないで積み上げて大小比較でよい
    """
    ts = sorted(ts, reverse=1)
    a1, a2 = 0, 0
    for i, t in enumerate(ts):
        if a1 > a2:
            a2 += t
        else:
            a1 += t
        print(i, t, a1, a2, file=sys.stderr)

    print(max(a1, a2))


def search(N, ts):
    total_t = sum(ts)
    ans = total_t
    for i in range(1 << N):
        s1 = sum(ts[j] * (i >> j & 1) for j in range(N))
        t = max(s1, total_t - s1)
        print(i, s1, total_t-s1, file=sys.stderr)
        ans = min(ans, t)

    print(ans)


def WA(N, ts):
    """
    時間がかかるものから
    """
    ts = sorted(ts, reverse=True)
    ans = ts[0]
    if N <= 2:
        print(ans)
        return

    diff = ts[0] - ts[1]
    for i in range(2, N):
        if diff - ts[i] >= 0:
            diff = - ts[i]
        else:
            diff = ts[i] - diff
            ans += diff

    print(ans)


if __name__ == '__main__':
    main()
