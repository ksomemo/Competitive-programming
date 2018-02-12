def main():
    N, K = map(int, input().split())

    ans = editorial(N, K)
    print(ans)


def editorial(N, K):
    """
    一番左の塗り方: K通り
    残りN-1個
        上記隣: 上記以外のK-1通り
        上記隣: 上記以外のK-1通り(一番左に塗った色復帰)
    """
    return K * (K-1) ** (N-1)


def WA(N, K):
    if N == 1:
        return K


if __name__ == '__main__':
    main()
