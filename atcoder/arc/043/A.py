def main():
    """
    Q:
        全体の底上げなので
        平均に影響する
        rangeに影響しない
    sum(P * Si + Q) / N = A
      avg(Si) * P + Q = A
      Q = A - avg(Si) * P

    max(P * Si + Q) - min(P * Si + Q) = B
    """
    N, A, B = map(int, input().split())
    S = [int(input()) for _ in range(N)]

    AC(N, A, B)


def AC(N, A, B):
    N, A, B = map(int, input().split())
    S = [int(input()) for _ in range(N)]

    _min = min(S)
    _max = max(S)
    r = _max-_min
    e = 10 ** -6
    # (m-m)*P≒B
    if r == 0:
        print(-1)
        quit()

    P = B/r

    _sum = sum(s*B for s in S) / r
    avg = _sum/N
    Q = A - avg

    print(P, Q)


if __name__ == '__main__':
    main()
