def main():
    """
    """
    N, M, Q = map(int, input().split())
    L, R = zip(*(
        map(int, input().split())
        for _ in range(M)
    ))
    p, q = zip(*(
        map(int, input().split())
        for _ in range(Q)
    ))

    # answers = f(N, M, Q, L, R, p, q)
    # experiment(N, M, Q, L, R, p, q)
    # answers = TLE(N, M, Q, L, R, p, q)
    answers = editorial_2(N, M, Q, L, R, p, q)
    for ans in answers:
        print(ans)


def editorial_2(N, M, Q, L, R, p, q):
    """
    ２次元累積和のライブラリを持っておくとよいらしい
        確かに実装ミスりそう
    """
    t = [[0] * (N+1) for _ in range(N+1)]
    for l, r in zip(L, R):
        t[l][r] += 1

    # 二次元累積和
    # 積分画像と同じ
    for l in range(1, N+1):
        for r in range(1, N+1):
            t[l][r] += t[l][r-1]
    for l in range(1, N+1):
        for r in range(1, N+1):
            t[l][r] += t[l-1][r]

    answers = []
    for l, r in zip(p, q):
        # https://twitter.com/iwashi31/status/1030823356579250178
        # memo[R][R] - memo[L-1][R] で十分な理由は、L <= R だから
        ans = 0
        ans += t[r][r]
        ans -= t[l-1][r]
        ans -= t[r][l-1]
        ans += t[l-1][l-1]

        answers.append(ans)

    return answers


def editorial_1(N, M, Q, L, R, p, q):
    # Lごとの累積和
    t1 = [[0] * (N+1) for _ in range(N+1)]
    t2 = [[0] * (N+1) for _ in range(N+1)]
    # LRの組合せ, N<=500より間に合う
    for l, r in zip(L, R):
        t1[l][r] += 1

    for l in range(1, N+1):
        for r in range(1, N+1):
            t2[l][r] = t2[l][r-1] + t1[l][r]

    answers = []
    for _p, _q in zip(p, q):
        ans = 0
        for l in range(_p, _q+1):
            ans += t2[l][_q] - t2[l][_p-1]

        answers.append(ans)

    return answers


def f(N, M, Q, L, R, p, q):
    """
    東西に１本の線路、都市: 1...N
    M本の列車: i列車 Li to Ri (L=Rのときもある)
    Q questions

    pi <= Lj and Rj <= qi

    1 <= N <= 500
    1 <= M <= 2 * 10^5
    1 <= Q <=     10^5
    1 <= Li <= Ri <= N (1 <= i <= M)
    1 <= pi <= qi <= N (1 <= i <= Q)
    """
    ans = 0
    return ans


def experiment(N, M, Q, L, R, p, q):
    """
    https://beta.atcoder.jp/contests/abc103/tasks/abc103_d
    上記を思い浮かべたけど、ちょっと違う
    """
    # 各都市に止まれる列車の数: 利用できなさそう＋TLE
    cumsum = [0] * (N + 1)
    for left, right in zip(L, R):
        for i in range(left, right+1):
            cumsum[i] += 1
    print("\t", cumsum)

    import numpy as np
    cumsum = np.zeros(N+1, dtype=int)
    for left, right in zip(L, R):
        cumsum[left:right+1] += 1
    print("\t", cumsum)

    # 並べて実験
    pair = [
        (l, r)
        for l, r in sorted(zip(L, R), key=lambda x: -x[1])
    ]
    print("\t", "".join(map(lambda x: str(x)[-1], range(1, N+1))))
    for l, r in pair:
        print("\t ", " " * (l - 1), "-" * (r - l + 1), sep="")

    print("\t", pair)

    print("\t",
          [
              abs(cumsum[l] - cumsum[r])
              for _p, _q in zip(p, q)
          ]
          )


def TLE(N, M, Q, L, R, p, q):
    """
    10^5 * 10^5
    """
    answers = []
    for _p, _q in zip(p, q):
        ans = 0
        for left, right in zip(L, R):
            if _p <= left and right <= _q:
                ans += 1

        answers.append(ans)

    return answers


if __name__ == '__main__':
    main()
