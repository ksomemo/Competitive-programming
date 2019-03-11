def main():
    N, A, B, C = map(int, input().split())
    ls = [int(input()) for _ in range(N)]

    ans = editorial(N, A, B, C, ls)
    print(ans)


def editorial(N, A, B, C, ls):
    def dfs(cur, a, b, c):
        if cur == N:
            if min([a, b, c]) > 0:
                # 使わなくて足りない/使いすぎて超過している分は差引すればいい
                tmp = abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                tmp = float("inf")
            # print(tmp, a, b, c, sep="\t")
            return tmp

        # 使うか使わないか,合成パターンを試す
        d = ls[cur]
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + d, b, c) + 10
        ret2 = dfs(cur + 1, a, b + d, c) + 10
        ret3 = dfs(cur + 1, a, b, c + d) + 10

        return min([ret0, ret1, ret2, ret3])

    ans = dfs(0, 0, 0, 0)
    return ans


def WA(N, A, B, C, ls):
    tmp = []
    from itertools import permutations
    for a, b, c in permutations([A, B, C]):
        x = f(N, a, b, c, ls)
        tmp.append(x)

    ans = min(tmp)
    print(ans)


def f(N, A, B, C, ls):
    """
    A,B,Cそれぞれが存在していたら終了
    存在しない場合
    diff をとる
        diffと合成するしないでの最善
    ABCの順に依存するが、3つしかないので 3P3=6通り
    N_max=8 よりゴリ押し
    """
    ls = ls[:]
    abc = [A, B, C]

    ans = 0
    for x in abc[:]:
        if x in ls:
            abc.remove(x)
            ls.remove(x)

    while abc:
        x = abc[0]
        diffs = [l - x for l in ls]
        # print(abc, ans, ls, diffs)
        # 完全一致
        if x in ls:
            ls.remove(x)
            abc.remove(x)
            continue

        # 合成コスト以下, sortedで試してたけどmin のkey指定でよかった
        i, diff = min(enumerate(diffs), key=lambda a: abs(a[0]))
        min_cost = abs(diff)
        if min_cost <= 10:
            ans += min_cost
            del ls[i]
            del abc[0]
            continue

        # 合成できない
        if len(ls) < 2:
            ans += abs(ls[0] - x)
            abc.remove(x)
            del ls[0]
            continue

        # 合成
        comb = []
        n_ls = len(ls)
        for i in range(n_ls):
            for j in range(i+1, n_ls):
                comb.append((i, j, ls[i] + ls[j]))

        # 合成前後のコスト比較
        i, j, new_l = min(comb, key=lambda b: abs(b[2] - x))
        # print("\t", [c[2] for c in comb])
        # print("\t", i, j, new_l, min_cost)
        cost = abs(x - new_l)
        if cost >= min_cost:
            del_idx = min(i, j, key=lambda idx: abs(ls[idx]) - x)
            ans += min_cost
            del ls[del_idx]
            del abc[0]
        else:
            ls[i] = new_l
            del ls[j]
            ans += 10

    return ans


if __name__ == '__main__':
    main()
