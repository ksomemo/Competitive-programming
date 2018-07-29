def main():
    """
    2 <= N <= 10^5
    1 <= M <= 10^5
    1 <= ai < bi <= N
    (ai, bi) != (aj, bj)
    """
    N, M = map(int, input().split())
    A, B = zip(*[
        map(int, input().split())
        for _ in range(M)
    ])
    # ans = WA(N, M, A, B)
    ans = editorial(N, M, A, B)
    # ans = TLE(N, M, A, B)

    print(ans)


def editorial(N, M, A, B):
    """
    区間スケジューリング
    https://twitter.com/yfba_/status/1020667765340831744
    https://twitter.com/evima0/status/1020665424998903809
    https://twitter.com/eiya5498513/status/1020667212749684736
        詳しい考察
    https://twitter.com/satanic0258/status/1020670048468271104
        終点ソートして手前のものからとっていくのが明らかに最適

    https://twitter.com/threecourse/status/1020667755857506309
        ただの区間スケジューリングか。。。とても怪しい解き方をした
        https://beta.atcoder.jp/contests/abc103/submissions/2887313

    https://twitter.com/tempura_pp/status/1020671041759109120
        実装簡単にできるらしい

    https://twitter.com/koyumeishi_/status/1020673642160517126
        nodeとedgeっぽいのでグラフからのフローと考える
        node:N,edge:N-1 より木、そこから木DP、という考え方があるらしい
        結局は貪欲
    https://twitter.com/m_buyoh/status/1020666105881288705
        こちらもフローで考え始めたらしい(最大流・最小カット)
    https://twitter.com/homesentinel214/status/1020664698901954560
        segment tree でもできるらしい(なぜか知りたい)
    https://twitter.com/drken1215/status/1020669263839805440
        双対問題？
        ・最小カット問題：最大流問題の双対問題
        ・牛ゲー：最短路問題の双対問題
        ・最小費用流問題の双対問題：最小費用流問題の双対問題 (競プロ最高難度で定番)
        ・今日の D：区間スケジューリング問題の双対問題
            http://drken1215.hatenablog.com/entry/2018/07/21/224200

            まず区間スケジューリング問題の答えが k 個だった場合、
            それらを全部刺すには最低でも k 本の串が必要である (弱双対性)
            ↓
            ・具体的に k 本の串で刺せることを構成的に示す (強双対性)
            みたいな流れは、双対性を扱う定番の流れ

            Ford-Fulkerson 法のような最大フローアルゴリズムが
            なんで正しく最大フローを求めることができるのか
            の証明のロジックも非常によく似ている
    """
    ans1 = AC_b_sort(N, M, A, B)
    ans2 = AC_a_sort(N, M, A, B)
    assert ans1 == ans2
    return ans1


def AC_b_sort(N, M, A, B):
    ab = sorted(zip(A, B), key=lambda x: (x[1], x[0]))
    ans = 0
    bef_b = 0
    for a, b in ab:
        # print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_b <= a:
            ans += 1
            bef_b = b

    return ans


def AC_a_sort(N, M, A, B):
    ab = sorted(zip(A, B), key=lambda x: (x[0], -x[1]))
    ans = 0
    bef_b = float("inf")
    for a, b in ab:
        # print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_b <= a:
            ans += 1
            bef_b = b
        else:
            bef_b = min(bef_b, b)

    return ans + 1


def TLE(N, M, A, B):
    """
    """
    ans = N - 1
    for a in A:
        for b in B:
            pass

    return ans


def WA(N, M, A, B):
    """
    ai, bi の分断:

    入力例1
        1, 4 の分断
            橋1-3 のどれかを除去
        2, 5 の分断
            橋2-4 のどれかを除去
        共通部: 2-3
        要望ごとの共通部を探す必要がある
            M^2: TLE

    A_min: 西
    A_max: 東
    B_min: 西
    B_max: 東

    入力例2
    9 5
    1------8
     2----7
      3-5
       4-6
          7-9

    a_min,b_max の順に並べる
    要望の東側が以前の西側未満ならOK
    要望の西側が以前の東側を超えないならOK ?
    """
    ab = sorted(zip(A, B), key=lambda x: (x[0], -x[1]))
    ans = 0
    bef_a, bef_b = -1, float("inf")
    for i, (a, b) in enumerate(ab):
        print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_a <= a < b <= bef_b:
            pass
        elif bef_b <= a:
            ans += 1
        elif bef_a < a < bef_b < b:
            pass

        bef_a, bef_b = a, b

    return ans + 1


if __name__ == '__main__':
    main()
