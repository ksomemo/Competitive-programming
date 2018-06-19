import sys
import heapq
from collections import deque
sys.setrecursionlimit(10 ** 7)


def main():
    """
    1 <= N <= 10^5
    """
    N = int(input())

    ans = f(N)
    print(ans)


def assert_ans(f):
    N_ans = [
        (127, 4),
        (3, 3),
        (44852, 16),
    ]
    for N, ans in N_ans:
        assert f(N) == ans


def test_rec():
    pass
    # zsh: segmentation fault in my pc, AC in AtCoder
    # assert_ans(rec)


def test_bfs():
    assert_ans(bfs)


def test_all_search():
    assert_ans(editorial_pdf)


def test_dp_atsumeru():
    assert_ans(editorial_movie)


def test_dp_kubaru():
    assert_ans(dp_kubaru)


def test_napsack():
    assert_ans(napsack)


def test_search_heap():
    assert_ans(search_heap)


def test_dijkstra():
    assert_ans(dijkstra)


def bfs(N):
    """
    https://qiita.com/drken/items/ace3142967c4f01d42e9#%E8%A7%A3%E6%B3%95-4-%E5%85%A8%E6%8E%A2%E7%B4%A2--greedy
    """
    memo = [-1] * (N+1)
    memo[0] = 0

    q = deque([0])
    while q:
        v = q.popleft()

        p = 1
        while v + p <= N:
            if memo[v + p] == -1:
                memo[v + p] = memo[v] + 1
                q.append(v + p)
            p *= 6

        p = 1
        while v + p <= N:
            if memo[v + p] == -1:
                memo[v + p] = memo[v] + 1
                q.append(v + p)
            p *= 9

    return memo[N]


class Edge:
    def __init__(self, from_v, to_v, cost):
        self.from_v = from_v
        self.to_v = to_v
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class Vertex:
    def __init__(self, cost, id):
        self.cost = cost
        self.id = id

    def __lt__(self, other):
        return self.cost < other.cost


class Dijkstra:
    def __init__(self, n_v):
        self.g = [[] for _ in range(n_v)]
        self.n_v = n_v
        self.dists = []

    def add_edge(self, from_v, to_v, cost):
        e = Edge(from_v, to_v, cost)
        self.g[from_v].append(e)

    def calc_shortest_dists(self, start):
        self.dists = [float("inf")] * self.n_v
        self.dists[start] = 0

        q = []
        heapq.heappush(q, Vertex(0, start))

        while q:
            top = heapq.heappop(q)
            if self.dists[top.id] < top.cost:
                continue

            for e in self.g[top.id]:
                prev_cost = self.dists[e.from_v]
                next_cost = self.dists[e.to_v]
                if next_cost > prev_cost + e.cost:
                    next_cost = prev_cost + e.cost
                    self.dists[e.to_v] = next_cost
                    heapq.heappush(q, Vertex(next_cost, e.to_v))


def dijkstra(N):
    """
    queue.PriorityQueue は heapq より遅いの改良
    自作classに __lt__を作成して順序について気にしないようにできる

    https://twitter.com/homesentinel214/status/1005806973214789635
    https://beta.atcoder.jp/contests/abc099/submissions/2651720
    """
    d = Dijkstra(N + 1)
    for i in range(N + 1):
        d.add_edge(i, i - 1, 1)

        j = 6
        while j <= i:
            d.add_edge(i, i - j, 1)
            j *= 6

        j = 9
        while j <= i:
            d.add_edge(i, i - j, 1)
            j *= 9

    # N to 0 の最短経路
    d.calc_shortest_dists(N)
    ans = d.dists[0]
    return ans


def search_heap(N):
    """
    これもDijkstra
        というより、priority_queue を使うらしい
    https://twitter.com/_TTJR_/status/1005806878788472833
        合計を頂点、6^k ・ 9^k 足すのを辺とみなして最短路
    https://beta.atcoder.jp/contests/abc099/submissions/2649257
    https://docs.python.jp/3/library/heapq.html
    """
    costs = [N] * (N+1)
    costs[0] = 0
    q = []
    heapq.heappush(q, 0)

    # ここから
    while q:
        e = heapq.heappop(q)

        w = 1
        while e + w <= N:
            if costs[e + w] > costs[e] + 1:
                costs[e + w] = costs[e] + 1
                heapq.heappush(q, e + w)
            w *= 6

        w = 9
        while e + w <= N:
            if costs[e + w] > costs[e] + 1:
                costs[e + w] = costs[e] + 1
                heapq.heappush(q, e + w)
            w *= 9

    return costs[N]

    # TODO: 下記の意味は？
    ans = N
    for i in range(N+1):
        ans = min(ans, costs[i] + (N - i))

    return ans


def napsack(N):
    """
    https://qiita.com/drken/items/ace3142967c4f01d42e9#%E8%A7%A3%E6%B3%95-4-%E5%85%A8%E6%8E%A2%E7%B4%A2--greedy
    6^p を何回でも使える
    """
    ws = []
    w = 1
    while w <= N:
        ws.append(w)
        w *= 6
    w = 9
    while w <= N:
        ws.append(w)
        w *= 9

    ans1 = napsack_solve1(N, ws)
    ans2 = napsack_solve1(N, ws)
    assert ans1 == ans2

    return ans1


def napsack_solve1(N, ws):
    n = len(ws)
    dp = []
    for i in range(n + 1):
        dp.append([float("inf")] * (N+1))
        dp[i][0] = 0

    for i in range(n):
        for w in range(N + 1):
            dp[i+1][w] = min(dp[i+1][w], dp[i][w])
            if w >= ws[i]:
                dp[i+1][w] = min(dp[i+1][w],
                                 dp[i+1][w - ws[i]] + 1)

    return dp[n][N]


def napsack_solve2(N, ws):
    n = len(ws)
    dp = [float("inf")] * (N+1)
    dp[0] = 0

    for i in range(n):
        for w in range(N + 1):
            dp[w] = min(dp[w], dp[w - ws[i]] + 1)

    return dp[n][N]


def rec(N):
    """再帰

    フィボナッチ数と同じ感覚でさかのぼっている
    停止条件に加えて、初期値に気をつける必要がある
    """
    memo = [-1] * (N+1)

    def _rec(i):
        if i == 0:
            return 0
        if memo[i] != -1:
            return memo[i]

        ans = N
        p = 1
        while p <= i:
            ans = min(ans, _rec(i-p) + 1)
            p *= 6
        p = 1
        while p <= i:
            ans = min(ans, _rec(i-p) + 1)
            p *= 9

        memo[i] = ans

        return ans

    return _rec(N)


def editorial_pdf(N):
    """
    https://twitter.com/chokudai/status/1005820807472242688

    6^p * 6 == 6^(p+1)
    N円のうち、6系と9系で払う金額の組合せを考える
        i円を6系
        N-iを9系
    """
    ans = N
    for i in range(N+1):
        cc, t = 0, i
        while t > 0:
            """
            この方法で、6^1以上のべき乗で表せない数値から払っていることになる
            他の方法: https://beta.atcoder.jp/contests/abc099/submissions/2648032

            e.g: 36
            36 % 6 == 0, 36 // 6 == 6
             6 % 6 == 0,  6 // 6 == 1
             1 % 6 == 1,  1 // 6 == 0

            e.g: 51
                3: 1 * 6^2 + 2 * 6^1 + 3 * 6^0
                2: 1 * 6^1 + 2 * 6^0
                1: 1 * 6^0
            51 % 6 == 3, 51 // 6 == 8
             8 % 6 == 2,  8 // 6 == 1
             1 % 6 == 1,  1 // 6 == 0
            """
            cc += t % 6
            t //= 6

        t = N - i
        while t > 0:
            cc += t % 9
            t //= 9

        ans = min(ans, cc)

    return ans


def editorial_movie(N):
    """
    DP(集める)
    """
    dp = [N] * (N+1)
    dp[0] = 0

    for i in range(1, N+1):
        p = 1
        while p <= i:
            dp[i] = min(dp[i], dp[i-p] + 1)
            p *= 6

        p = 1
        while p <= i:
            dp[i] = min(dp[i], dp[i-p] + 1)
            p *= 9

    return dp[N]


def dp_kubaru(N):
    """
    DP(配る)
    """
    dp = [N] * (N+1)
    dp[0] = 0

    # 範囲が集める時と異なる(i+pなので当たり前+p=1から始まるため)
    for i in range(N):
        p = 1
        while i + p <= N:
            dp[i+p] = min(dp[i+p], dp[i] + 1)
            p *= 6

        p = 1
        while i + p <= N:
            dp[i+p] = min(dp[i+p], dp[i] + 1)
            p *= 9

    return dp[N]


def f(N):
    """
    1: 1回
    6^n, 9^n: n回

    「ちょうど」払う

    N円ちょうど払うときの最小回数
    1円で払えばN円のときN回
    N円以下の組合せによる最小回数

    例:
        2〜5: 2,3,4,5
        6: 1
        7,8: 2,3
        9: 1
        10〜14: 2,3,4,5
        15: 2

        15=14+1
          =13+2
          =12+3
          =11+4
          =10+5
          = 9+6
    """
    x = [i for i in range(N+1)]
    x = [0] * (N+1)
    x[1] = 1
    a, b = 6, 9
    while a <= N or b <= N:
        if a <= N:
            x[a] = 1
        if b <= N:
            x[b] = 1
        a, b = a * 6, b * 9

    return WA2(N, x)
    return WA1(N, x)


def WA2(N, x):
    for i in range(2, N+1):
        m = 0
        k = i
        for j in range(i, 0, -1):
            if x[j] > 0:
                # 払えるので、残り金額を引く
                c = k // j
                k -= c * j
                # 回数更新
                m += x[j] * c
            if k == 0:
                break
        x[i] = m

    ans = x[N]
    return ans


def WA1(N, x):
    e = N
    ans = 0
    for y, ok in list(enumerate(x))[::-1]:
        if ok:
            c = e // y
            ans += c
            e -= c * y
            if N == 0:
                break

    return ans


if __name__ == '__main__':
    main()
