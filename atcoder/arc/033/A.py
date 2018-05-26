def main():
    N = int(input())

    ans = AC(N)
    print(ans)


def test_ans():
    assert AC(1) == editorial3(1)
    assert AC(2) == editorial3(2)
    assert AC(3) == editorial3(3)
    assert AC(4) == editorial3(4)


def AC(N):
    ans = 0
    for i in range(1, N+1):
        ans += N - i + 1

    return ans


def editorial3(N):
    """
    解説通り 繰り返しの性質を見ることで
    N=1: 1
    N=2: 3
    N=3: 6
    N=4: 10
    より、1+2+...+N = N(N+1)/2 でO(1)
    """
    return N * (N + 1) // 2


if __name__ == '__main__':
    main()
