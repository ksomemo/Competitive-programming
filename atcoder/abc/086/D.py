def main():
    """
    Range:
        (x,y)
        X: x-K+1 〜 x+K-1
        Y: y-K+1 〜 y+K-1

    rangeをすべて試す: 無理
        1つの希望を満たすように範囲指定:
            模様は確定する
                (0,0)-(K,K) * 2(W or B)
                K^2 * N -> 10^3^2 * 10^5
            他の希望は満たされるか判定
        他の範囲指定で満たされるか
            組合せ膨大すぎる
    """
    N, K = map(int, input().split())
    xyc = [
        input().split()
        for _ in range(N)
    ]

    TLE(N, K, xyc)


def TLE(N, K, xyc):
    ans = 0
    for i in range(2 * K):
        for j in range(2 * K):
            tmp_ans = 0
            for x, y, c in xyc:
                x = int(x) % (2 * K)
                y = int(y) % (2 * K)

                w1 = i <= x < i + K and j <= y < j + K
                w2 = i + K <= x < i + 2 * K and j + K <= y < j + 2 * K

                print(i, j, x, y, c, w1, w2, sep="\t")
                if w1 or w2:
                    if c == "W":
                        tmp_ans += 1
                else:
                    if c == "B":
                        tmp_ans += 1

            ans = max(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()
