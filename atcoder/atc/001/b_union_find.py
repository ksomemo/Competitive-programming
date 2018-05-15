import sys


def main():
    N, Q = map(int, input().split())
    par = list(range(N))
    i_l_list = [
        list(map(int, input().split()))
        for _ in range(Q)
    ]

    uf = UnionFind(par)
    func(N, Q, par, i_l_list, uf)


def func(N, Q, par, i_l_list, uf=None):
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]

    def same(x, y):
        return root(x) == root(y)

    def unite(x, y):
        x = root(x)
        y = root(y)

        if x != y:
            par[y] = x

    print(par, end='', file=sys.stderr)
    if uf is not None:
        root = uf.root
        same = uf.same
        unite = uf.unite
        par = uf.par

    for l in i_l_list:
        q_type, a, b = l
        if q_type == 0:
            unite(a, b)
            print(par, end='', file=sys.stderr)
            print('concat', file=sys.stderr)
        else:
            is_same = same(a, b)
            print(par, end='', file=sys.stderr)
            print('judge:', file=sys.stderr)
            if is_same:
                print('Yes')
            else:
                print('No')


class UnionFind:
    """
    ランクなし

    https://www.slideshare.net/chokudai/union-find-49066733
    http://topcoder.g.hatena.ne.jp/iwiwi/20131226/1388062106
    http://pakapa104.hatenablog.com/entry/2016/02/04/233326
    """

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


if __name__ == '__main__':
    main()
