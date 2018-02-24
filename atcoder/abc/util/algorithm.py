from collections import deque


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


def dfs_bfs():
    """
    dfs/bfs maze matrix and graph
    """
    graph_main()
    array_main()


def array_main():
    """
    SからGを探す
    ■は通れる
    □は通れない
    """
    maze_str = """
        Ｓ■■■■□
        □■□□□■
        ■■■□■■
        ■□■□■□
        ■□■■■□
        ■□■□■Ｇ
    """
    start = (0, 0)
    goal = (5, 5)

    maze = maze_str.splitlines()
    maze = map(lambda x: list(x.strip()), maze)
    maze = [line for line in maze if line]

    print("dfs_array", "-"*10)
    visited = visited_maze(maze)
    dfs_array(maze, visited, start, goal)

    print("bfs_array", "-"*10)
    visited = visited_maze(maze)
    bfs_array(maze, visited, start, goal)


def visited_maze(maze):
    visited = [
        [0 for _ in l]
        for l in maze
    ]
    return visited


def graph_main():
    """
    (1)-(2)--(3)--(6)
           |_(4)--(7)
           |    |_(8)
           |_(5)--(9)

    1から開始して8を探す
    """
    graph = {
        1: [2],
        2: [3, 4, 5],
        3: [6],
        4: [7, 8],
        5: [9],
    }
    start = 1
    goal = 8

    print("dfs_graph", "-"*10)
    dfs_graph(graph, start, goal)

    print("bfs_graph", "-"*10)
    bfs_graph(graph, start, goal)

    print("dfs_graph_rec", "-"*10)
    found = dfs_graph_rec(graph, start, goal)
    print("found:", found)


def dfs_graph_rec(graph, start, goal):
    print(start)
    if start == goal:
        return True

    for v in graph.get(start, []):
        if dfs_graph_rec(graph, v, goal):
            return True

    return False


def dfs_graph(graph, start, goal):
    stack = []
    for x in graph.get(start, []):
        stack.append(x)

    print("start:", start)
    while stack:
        v = stack.pop()
        print(v)
        if v == goal:
            print("found")
            return
        for x in graph.get(v, []):
            stack.append(x)

    print("not found")


def movable_pos(x, y, W, H):
    pos = []
    for dx in (-1, 1):
        if 0 <= x + dx < W:
            pos.append((x+dx, y))
    for dy in (-1, 1):
        if 0 <= y + dy < W:
            pos.append((x, y+dy))

    return pos


def dfs_array(maze, visited, start, goal):
    (sx, sy) = start
    visited[sy][sx] = 1
    W, H = len(maze[0]), len(maze)

    stack = []
    for x, y in movable_pos(sx, sy, W, H):
        if visited[y][x] or maze[y][x] == "□":
            continue
        stack.append((x, y))

    while stack:
        x, y = stack.pop()
        print(y, x)
        visited[y][x] = 1
        if (x, y) == goal:
            print("found")
            return

        for mx, my in movable_pos(x, y, W, H):
            if visited[my][mx] or maze[my][mx] == "□":
                continue
            stack.append((mx, my))

    print("not found")


def bfs_array(maze, visited, start, goal):
    (sx, sy) = start
    visited[sy][sx] = 1
    W, H = len(maze[0]), len(maze)

    queue = deque()
    for x, y in movable_pos(sx, sy, W, H):
        if visited[y][x] or maze[y][x] == "□":
            continue
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        print(y, x)
        visited[y][x] = 1
        if (x, y) == goal:
            print("found")
            return

        for mx, my in movable_pos(x, y, W, H):
            if visited[my][mx] or maze[my][mx] == "□":
                continue
            queue.append((mx, my))

    print("not found")


def bfs_graph(graph, start, goal):
    queue = deque()
    for x in graph.get(start, []):
        queue.append(x)

    print("start:", start)
    while queue:
        v = queue.popleft()
        print(v)
        if v == goal:
            print("found")
            return
        for x in graph.get(v, []):
            queue.append(x)

    print("not found")


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
    N = 7
    start = 0
    goal = 6
    edges = [
        (0, 1, 9),
        (0, 2, 2),
        (2, 1, 6),
        (1, 4, 1),
        (1, 3, 3),
        (2, 3, 2),
        (2, 5, 9),
        (3, 4, 5),
        (3, 5, 6),
        (5, 4, 3),
        (5, 6, 4),
        (4, 6, 7),
    ]
    solove_bellmanford(N, start, goal, edges)

    N = 4
    start = 0
    goal = 3
    edges = [
        (0, 1, 2),
        (1, 0, 1),
        (0, 2, 4),
        (2, 1, 3),  # idx:3, change when after problems
        (1, 3, 1),
        (2, 3, 1),
    ]

    print("-"*10)
    print("directed:")
    solove_bellmanford(N, start, goal, edges, directed=True)

    print("-"*10)
    print("directed contains muinus:")
    edges[3] = (2, 1, -3)
    solove_bellmanford(N, start, goal, edges, directed=True)

    print("-"*10)
    print("directed contains muinus cycle:")
    edges[3] = (2, 1, -6)
    solove_bellmanford(N, start, goal, edges, directed=True)


def solove_bellmanford(N, start, goal, edges, directed=False):
    cost = [float("inf") for _ in range(N)]
    cost[start] = start
    con = [-1] * N
    con[start] = start

    m_cycle = 0
    for i in range(N):
        up = 0
        for edge in edges:
            src,  dst, e = edge

            if cost[dst] > cost[src] + e:
                cost[dst] = cost[src] + e
                up = 1
                con[dst] = src

            if not directed:
                if cost[src] > cost[dst] + e:
                    cost[src] = cost[dst] + e
                    con[src] = dst
                    up = 1

        if up == 0:
            break
        elif i == N-1:
            m_cycle = 1

    path = [goal]
    dst = goal
    while True:
        src = con[dst]
        if src == 0:
            break
        else:
            path.append(src)
        dst = src

    print("cost:", cost)
    print("connection:", con)
    print("reversed path to goal:", path)
    print("muinus cycle", m_cycle)


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
