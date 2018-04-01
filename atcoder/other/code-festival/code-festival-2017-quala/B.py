def main():
    N, M, K = map(int, input().split())

    editorial(N, M, K)

def editorial(N, M, K):
    for k in range(N+1):
        for l in range(M+1):
            # 黒の面積
            # 選択行数 * (列 - 選択列数)
            x = k * (M - l) + (N - k) * l
            if x == K:
                print("Yes")
                return

    print("No")

def WA(N, M, K):
    """
    0行変更：0
    1行変更：N
        特別判定(loopから除外)
    1行変更、1列変更：1つだけ戻る
        N +  M - 2
        (N - 1) + (M - 1)
    2行変更、1列変更：2つだけ戻る
        2N + M - 4
        (2N - 2) + (M - 2)
    2行変更、2列変更：4つだけ戻る
        2N + 2M - 8
        (2N - 4) + (2M - 4)
    """

    # 行/列のみで対処可能か
    if K % N == 0 or K % M == 0:
        print("Yes")
        return

    # 行/列のみを除外
    for n in range(1, N+1):
        for m in range(1, M+1):
            x = n * N + m * M - (2 * n * m)
            if x == K:
                print("Yes")
                return

    print("No")


if __name__ == '__main__':
    main()
