def main():
    """
    ワーシャルフロイドで経由したときに変更がないことを確認する
    変更がある場合、
        最短経路ではないため条件を満たさない
    変更がない場合、
        経由の経路でも最短距離になるケースを除いて距離を計算する
    """
    N = int(input())
    a = [None] * N
    total = 0
    for i in range(N):
        a[i] = list(map(int, input().split()))
        total += sum(a[i])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                # compare from-to / from-経由地点-to
                d = a[i][k] + a[k][j]
                if a[i][j] > d:
                    return -1

    # 不要判定
    v = [[False] * N for _ in range(N)]
    no_need = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == k or j == k:
                    continue
                if not v[i][j] and (a[i][j] == a[i][k] + a[k][j]):
                    no_need += a[i][j]
                    v[i][j] = True

    # 対称なので半分にする
    return (total - no_need) // 2

if __name__ == '__main__':
    answer = main()
    print(answer)
