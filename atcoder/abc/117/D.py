def main():
    A, B, Q = map(int, input().split())
    ss = [int(input()) for _ in range(A)]
    ts = [int(input()) for _ in range(B)]
    xs = [int(input()) for _ in range(Q)]

    ans = editorial(A, B, Q, ss, ts, xs)
    print(ans)


def editorial(A, B, Q, ss, ts, xs):
    """
    """
    ans = 0
    return ans


if __name__ == '__main__':
    main()
