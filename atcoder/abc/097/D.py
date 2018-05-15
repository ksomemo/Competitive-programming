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

    editorial(N, M, p, xy)


class UnionFind:
    def __init__(self, par):
        self.par = par

    def root(self, x):
        if self.par[x] == x:
            return x
        # 経路圧縮
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x != y:
            self.par[y] = x


def editorial(N, M, p, xy):
    par = list(range(N+1))
    uf = UnionFind(par)
    for x, y in xy:
        uf.unite(x, y)

    _p = [0] + p
    ans = 0
    for i in range(1, N+1):
        if uf.root(i) == uf.root(_p[i]):
            ans += 1

    print(ans)


def reference1(N, M, p, xy):
    """
    https://twitter.com/evima0/status/995302238548455430
    https://twitter.com/_TTJR_/status/995300529952600065
    https://twitter.com/yosupot/status/995301931772887041
    https://twitter.com/naoppy_ac/status/995301084322152448
    https://twitter.com/nomikura/status/995297915324153858

    入力例より、連結部分は入れ替え可能
    連結部分をグループとして見たいときはUnionFindが典型らしい

    union find使わなくてもできる
    →単純にグラフ構築し、連結判定をDFSで解決する(動画より)

    Cycleが含まれているとUnionFindとして使いにくい?
    →最小全域木にしてCycleを除外する
    """
    pass


def f2(N, M, p, xy):
    """
    https://beta.atcoder.jp/contests/abc097/submissions/2511659
    """
    from collections import defaultdict, deque
    g = defaultdict(list)
    for x, y in xy:
        g[x].append(y)
        g[y].append(x)

    ans = 0
    group = [0] * (N+1)
    # index付き
    for i, num in enumerate(p, 1):
        q = deque([i])
        while q:
            print(q, i, group)
            v = q.popleft()
            if group[v]:
                continue

            # groupに属している
            group[v] = i
            for v2 in g[v]:
                q.append(v2)

        ans += group[num] == group[i]

    print(ans)


def f1(N, g):
    """
    https://beta.atcoder.jp/contests/abc097/submissions/2500414
    """
    ans = 0
    visited = defaultdict(bool)
    for i in range(1, N):
        q = deque([i])
        vs = set()
        print("i:", i)
        while q:
            print("q:", q)
            src = q.popleft()
            if not visited[src]:
                for dst in g[src]:
                    q.append(dst)
                    vs.add(dst)
                    visited[dst] = True
        print("vs:", end="")
        pprint(vs)
        print("visited:", end="")
        pprint(visited)
        ans += 1


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
    for x, y in xy:
        if y in d_xy:
            extra.append((x, d_xy[y]))

    print(xy)
    print("---")
    print(extra)


if __name__ == '__main__':
    main()
