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
    for i in range(N):
        a[i] = list(map(int, input().split()))

    total = 0
    dist = {}
    for k in range(N):
        # from
        for i in range(N):
            # to
            for j in range(N):
                # compare from-to / from-経由地点-to
                d = a[i][k] + a[k][j]
                if a[i][j] > d:
                    return -1
                else:
                    dist[(i, j)] = d

    from pprint import pprint
    pprint(a)
    pprint(dist)

    return total


if __name__ == '__main__':
    answer = main()
    print(answer)
