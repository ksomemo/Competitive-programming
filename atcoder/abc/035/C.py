from collections import Counter


def main():
    """
    N,Q<=2*10^5

    Qの操作中にNすべて裏返す/列挙する等の処理をした時、
    NQより TLE
    """
    N, Q = map(int, input().split())
    LR = [
        list(map(int, input().split()))
        for _ in range(Q)
    ]

    # TLE(N, Q, LR)
    imos(N, Q, LR)


def imos(N, Q, LR):
    # N+1まで
    b = [0] * (N + 2)

    # 加算
    for l, r in LR:
        b[l] += 1
        b[r + 1] -= 1

    # 構築
    for i in range(1, N + 1):
        # -1 % 2 => 1, -2 % 2 => 0
        # 構築中でも構築として処理可能な場合があるっぽい
        b[i] %= 2
        b[i + 1] += b[i]

    ans = "".join(map(str, b[1:N + 1]))
    print(ans)


def TLE(N, Q, LR):
    c = Counter()
    for l, r in LR:
        c += Counter(range(l, r + 1))

    for i in range(1, N + 1):
        x = c[i]
        print(x % 2, end="")

    print("")


if __name__ == '__main__':
    main()
