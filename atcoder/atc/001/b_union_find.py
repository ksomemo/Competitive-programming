import sys


N, Q = map(int, input().split())
par = list(range(N))
i_l_list = [
    list(map(int, input().split()))
    for _ in range(Q)
]


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


print(par)
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
