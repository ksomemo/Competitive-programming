def bubble_sort():
    pass


def selection_sort():
    pass


def quick_sort():
    pass


def insertion_sort():
    pass


def merge_sort():
    pass


def heap_sort():
    pass


def a_star():
    pass


def dfs():
    pass


def bfs():
    pass


def bellmanford():
    """最短経路問題(始点あり)

    グラフの辺に負のコストがあっても使える
    O(E * V)
    始点から辺情報を元にコストの更新を行う
        更新前は始点から始点-始点はコスト0,その他の点間のコストは無限大
    始点につながる点から順に更新する
        コストが低くなれば更新(初回は、無限大なので必ず辺情報で更新される)
        どの点からの情報であるか保持
        逆方向もコストが低くなれば更新
    更新されなくなるまで続ける
        負の閉路があると無限に更新されるらしい
    """
    pass


def dijkstra():
    """最短経路問題(始点あり)

    グラフの辺が非負のときに使える
    O(E * logV)
    """
    pass


def warshall_floyd():
    """全点間の最短経路問題

    O(V^3)なので対応できないときがある
    V^3の理由は、a[i][j] と経由 a[i][k] + a[k][j] の比較による経路を求めるため
    ABCでも実際使ったことがある
    """
    pass


def cumulative_sum_method():
    """累積和法

    TODO 他に良い名前があればつけたい
    imos法も調べる
    """
    pass


def imos_1_0():
    """https://imoz.jp/algorithms/imos_method.html
    """
    # 0時~5時まで
    E = 5
    start = [1, 3, 2, 4]
    end = [4, 5, 4, 5]
    N = len(start)

    def no_imos():
        table = [0] * (E + 1)

        print("-" * 10)
        print("no_imos")
        print(table)

        for i in range(N):
            for t in range(start[i], end[i]):
                table[t] += 1
                print(i, t, table)

        return max(table)

    def imos():
        print("-" * 10)
        print("imos")

        table = [0] * (E + 1)
        for i in range(N):
            table[start[i]] += 1
            table[end[i]] -= 1
            print(i, table)

        for i in range(1, E + 1):
            table[i] += table[i - 1]
            print(i, table)

        return max(table)

    print(no_imos())
    print(imos())


def imos_2_1():
    """
    2 dimensions
    """
    W, H = 6, 6

    # x,y,edge length
    xyl = [
        (0, 0, 4),
        (1, 3, 2),
        (2, 2, 4),
    ]
    import os
    import time
    from pprint import pprint

    def clear():
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    def no_imos():
        tiles = [
            [0] * W
            for _ in range(H)
        ]

        for x, y, l in xyl:
            for _x in range(x, x + l):
                for _y in range(y, y + l):
                    tiles[_y][_x] += 1
                    clear()
                    print("no_imos")
                    print((x, y, l), _x, _y)
                    pprint(tiles)

        return max(max(row)for row in tiles)

    def imos():
        tiles = [
            [0] * (W + 1)
            for _ in range(H + 1)
        ]

        for x, y, l in xyl:
            tiles[y][x] += 1
            tiles[y][x + l] -= 1
            tiles[y + l][x] -= 1
            tiles[y + l][x + l] += 1

            clear()
            print("imos", (x, y, l))
            pprint(tiles)

        # W
        for y in range(H):
            for x in range(1, W):
                tiles[y][x] += tiles[y][x - 1]

                clear()
                print("imos", (x, y))
                pprint(tiles)
        # H
        for y in range(1, H):
            for x in range(W):
                tiles[y][x] += tiles[y - 1][x]

                clear()
                print("imos", (x, y))
                pprint(tiles)

        return max(max(row)for row in tiles)

    print(no_imos())
    input("Please press the Enter key, if start imos")
    print(imos())


def two_pointers():
    """しゃくとり法

    のことらしい。英語記事で見るらしい。
    https://twitter.com/satanic0258/status/839652558058635264
    """
    pass


def prim():
    """最小全域木のプリム法
    """
    pass


def kruskal():
    """最小全域木のクラスカル法
    """
    pass


def knapsack():
    pass
