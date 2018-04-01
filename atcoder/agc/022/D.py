def main():
    """
    1 <= N <= 300000
    1 <= L <= 10^9
    x: sorted, xi<xi+1, xN < L
    1 <= ti <= 10^9

    部分点: 1 <= N <= 3000
    """
    N, L = map(int, input().split())
    *X, = map(int, input().split())
    *T, = map(int, input().split())

    for x, t in zip(X, T):
        # 降りて列車が戻ってくるまで
        a = (L - x) * 2
        if t <= a:
            pass
        

if __name__ == '__main__':
    main()
