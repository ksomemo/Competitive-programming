def main():
    """今回得られる知見(解説より)

    – 負の重みがないグラフ(無向でも有向でも)においては
    • ある最短経路に現れる頂点は全て異なる
    • 最短経路は閉路を持たない
    """
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    P = map(int, input().split())

    ans = AC(a, b, P)
    if ans:
        print("YES")
    else:
        print("NO")


def AC(a, b, P):
    s = set([a, b])
    for p in P:
        if p in s:
            return False
        s.add(p)

    return True


def editorial2(a, b, P):
    P = sorted([a, b] + list(P))

    bef = P[0]
    for p in P[1:]:
        if p == bef:
            return False

    return True


def editorial3(a, b, N, P):
    c = [0] * (N+1)
    c[a] += 1
    c[b] += 1

    for p in P:
        c[p] += 1
    for i in c:
        if i >= 2:
            return False

    return True


if __name__ == '__main__':
    main()
