def main():
    """
    各街間の最小のコスト
    経由してきた場合と上記のコスト比較
       1 to 4:
         直接: 8
         間接: 6
            1 to 2: 1
            2 to 3: 2
            3 to 4: 3
    ある街からの最小コストで別の街へつなげたからと言って、
    すべての街を行き来できるとは限らない
    """
    N = int(input().strip())
    pos = [list(map(int, input().strip().split()))
           for i in range(N)]


def no_submittion(N, pos):
    for i in range(N):
        for k in range(i + 1, N):
            a, b = pos[i]
            c, d = pos[k]
            cost = min(abs(a - c), abs(b - d))
            print([i, k], cost, pos[i], pos[k])


if __name__ == '__main__':
    main()
