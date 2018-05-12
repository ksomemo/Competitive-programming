def main():
    """
    2 <= N <= 10^5
    1 <= M <= 10^5
    p: 順列

    1 <= xi, yi <= N
    xi != yj
    if i != j then {xi, yi} != {xj, yj}
    """
    N, M = map(int, input().split())
    *p, = map(int, input().split())
    xy = [
        list(map(int, input().split()))
        for _ in range(M)
    ]
    f(N, M, p, xy)


def f(N, M, p, xy):
    """
    (1, 2): 1,2を入れ替える
    (2, 3): 2,3を入れ替える
        default: 123
            1,2: 213
            2,3: 231
        defaultからの移動: (1,3), (1,2)
        (1,2),(2,3) -> (1,3),(1,2)
        入れ替えると2番目xが1番目xになる？

    入力例1より、j=1,2,1の順で入れ替え
        j1=(1,2),j2=(2,3) => (1,3)
    """
    d_xy = {x: y for x, y in xy}
    d_yx = {y: x for x, y in xy}
    extra = []
    for x,y in xy:
        if y in d_xy:
            extra.append((x, d_xy[y]))

    print(xy)
    print("---")
    print(extra)

if __name__ == '__main__':
    main()
