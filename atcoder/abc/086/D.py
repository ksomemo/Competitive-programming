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
    """
    N, K = map(int, input().split())
    xy = []
    for _ in range(N):
        x, y, c = input().split()
        a = K if c == "B" else 0
        xy.append((int(x), int(y) + a))

    TLE(K, xy)


def TLE(K, xy):
    ans = 0
    for i in range(2 * K):
        for j in range(2 * K):
            tmp_ans = 0
            for x, y in xy:
                x = (x + i) % (2 * K)
                y = (y + j) % (2 * K)

                w1 = x < K and y < K
                w2 = x >= K and y >= K
                if w1 or w2:
                    tmp_ans += 1

            ans = max(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()
