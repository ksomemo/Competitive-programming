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
    no_need = 0
    for i in range(N):
        a[i] = list(map(int, input().split()))
        total += sum(a[i])

    for k in range(N):
        # from
        for i in range(N):
            # to
            for j in range(N):
                # compare from-to / from-経由地点-to
                if i == k or j == k:
                    continue
                d = a[i][k] + a[k][j]
                if a[i][j] > d:
                    return -1
                elif a[i][j] == d:
                    # 経由して同じであれば必要ない
                    no_need += d

    # 対称なので半分にする
    return (total - no_need) // 2

if __name__ == '__main__':
    answer = main()
    print(answer)
