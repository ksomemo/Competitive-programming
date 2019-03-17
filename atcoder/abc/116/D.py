from collections import defaultdict


def main():
    """
    N個の寿司があり、それぞれの寿司には
    「ネタ」ti
    「おいしさ」di
    のパラメータが設定されています。 
    あなたはこの N個の寿司の中から K個を選んで食べようとしています。
    この時のあなたの「満足ポイント」は、以下のようにして計算されます。

    「満足ポイント」は、「おいしさ基礎ポイント」と、「種類ボーナスポイント」の和である。
    「おいしさ基礎ポイント」は、食べた寿司の「おいしさ」の総和である。
    「種類ボーナスポイント」は、食べた寿司の「ネタ」の種類数を xとしたとき、x ∗ x である。

    あなたは、「満足ポイント」をできるだけ大きくしたいです。
    この時の「満足ポイント」の値を求めてください。

    1 ≦ K  ≦ N ≦ 10^5
    1 ≦ ti ≦ N
    1 ≦ di ≦10^9

    nCk の組合せ: 10^5 C 10^5/2 => TLE
    DP ?
        1-Nまで, 食べる食べないによるスコア
        食べたとして種類数xとして種類は別途持っておく？
        →二次元配列は無理っぽそう, 10^5 * 10^5 = 10^10
        MAX時の種類だけ持って、１次元にする
        K までになっているかの判定
        →Nとは別に持たないといけない
    """
    N, K = map(int, input().split())
    td = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    ans = editorial(N, K, td)
    print(ans)


def editorial(N, K, td):
    td = sorted(td, key=lambda x: -x[1])
    c = defaultdict(int)
    d_sum = 0
    # 種類数が増えないので、不要と判断して良い基礎ポイント
    td_not_first = []
    for t, d in td[:K]:
        if c[t] > 0:
            td_not_first.append(d)
        c[t] += 1
        d_sum += d

    t_sum = len(c)
    ans = d_sum + t_sum ** 2

    for t, d in td[K:]:
        # 更新の余地なし
        if not td_not_first:
            return ans
        # すでに存在するなら、基礎ポイント降順のため不要
        if c[t] > 0:
            continue

        c[t] += 1
        d_sum += -td_not_first.pop() + d
        t_sum += 1
        ans = max(ans, d_sum + t_sum ** 2)

    return ans
    # ans = editorial_WA_TLE(N, K, td)


def editorial_WA_TLE(N, K, td):
    c = defaultdict(int)
    s = defaultdict(list)
    d_sum = 0
    for t, d in td[:K]:
        d_sum += d
        s[t].append(d)
        c[t] += 1
    t_sum = len(c)
    ans = d_sum + t_sum ** 2

    # print(ans)
    # print(td[:K])
    # print(td[K:])
    for t, d in td[K:]:
        # すでに存在するなら、基礎ポイント降順のため不要
        if c[t] > 0:
            continue

        for t2, count in c.items():
            # 基礎が大きく、1つしかないならば必要なので残す
            if count <= 1:
                continue

            # print((t, d), t2, s[t], s[t2], c[t], c[t2], d_sum, t_sum, sep="\t")
            # 消しても種類数が増えないものを除外して、種類数が増えるように調整
            ex = s[t2].pop()
            s[t].append(d)

            c[t] += 1
            c[t2] -= 1
            d_sum += -ex + d
            t_sum += 1
            # print((t, d), t2, s[t], s[t2], c[t], c[t2], d_sum, t_sum, sep="\t")

            tmp = d_sum + t_sum ** 2
            ans = max(ans, tmp)
            break

    return ans


def no_sub_WA(N, K, td):
    """
    td: 
    """
    # おいしさ貪欲でベースラインを作る
    td = sorted(td, key=lambda x: -x[1])
    td_k = td[:K]

    from collections import defaultdict, Counter
    td_rest = td[K:]
    ts, ds = zip(*[t_d for t_d in td_k])
    ts_counter = Counter(ts)
    x = len(ts_counter)
    ans = sum(ds) + x * x

    # おいしさ貪欲なので、
    # 同じ種類を入れ替えてもスコアは下がりボーナスは追加されない
    # 種類が増えるように入れ替える
    # 各種類で2つ以上存在するもの、その中でスコアが低いもの

    # rev sort済みなので末尾が最低スコアになり、都合が良い
    d_dict = defaultdict(list)
    for t, d in td_k:
        d_dict[t].append(d)
    print(ans, d_dict)

    # 一度の入れ替えでは更新されないが、
    # 続けて入れ替えすることで、種類が増えて更新されるため
    # 再帰にする必要がある
    # 愚直再帰では間に合わないので、priority queue を使う？
    for t_rest, d_rest in td_rest:
        exists_t = t_rest in ts_counter
        if exists_t:
            continue

        # 入れ替え候補
        td_min = []
        for t, _ in ts_counter.most_common(2):
            td_min.append((t, d_dict[t][-1]))
        if not td_min:
            continue
        t_old, d_old = sorted(td_min, key=lambda x: x[1])[0]
        print("\t", t_old, d_old)

        # (x + 1)^2 - x^2 = 2x + 1
        tmp = ans - d_old + d_rest + 2 * x + 1
        if tmp >= ans:
            ans = tmp
            x += 1
            ts_counter[t_rest] += 1
            ts_counter[t_old] -= 1
            d_dict[t_old].pop()
            d_dict[t_rest].append(d_rest)

            print(ans, d_dict)

    return ans


if __name__ == '__main__':
    main()
