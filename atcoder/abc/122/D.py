def main():
    N = int(input())

    ans = WA(N)
    print(ans)


def editorial(N):
    ans = 0
    return ans


def WA(N):
    """
    3 <= N <= 100
    4種類の文字: ACGT
    4^N 通りの文字列が存在する
    隣接文字2つを1回入れかることができる
    違反: AGC
    違反: 入力例1より
        ACG
        GAC

    2文字までは違反なし
    3文字では3つ違反, 上記の通り
        64-3 = 61
    4文字
        4文字目追加なので61 * 4
        3文字目の時点で3つで終わるパターンがある
        次に 下記パターンの文字が追加されるとNG
            AG C
            AC G
            GA C

        3文字のときに終わるパターンの構成
            AG: [.]AG NGなし    ACGT 4
            AC: [G]AC NGより    AC T 3 
            GA: [.]GA NGなし    ACGT 4

        AG: 構成4 * OK:4-1
        AC: 構成3 * OK:4-1
        GA: 構成4 * OK:4-1
            61 + (61 * 4 - [4+3+4] * 1)

        pattern に周期がありそう
        全パターンから引くので、逆元を使いそう
    """
    ans = 61
    ag_ac_ga = [4, 3, 4]
    if N == 3:
        return ans

    MOD = 10 ** 9 + 7
    for i in range(4, N+1):
        ag_ac_ga = [x * 3 for x in ag_ac_ga]
        print(ans + ans * i)
        print(sum(ag_ac_ga))
        ans += ans * i - sum(ag_ac_ga) * 3
        #ans = ans * i - sum(ag_ac_ga)

    ans %= MOD

    aaa()
    return ans


def aaa():
    ans = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    x = "".join(map(str, [i, j, k, l]))
                    # ACGT: 0123
                    # AGC, ACG, GAC
                    y = any(z in x for z in ("021", "012", "201"))
                    ans.append((x, y))

    print(*ans, sep="\n")
    print(sum(x[1] for x in ans))
    print(len(ans))


if __name__ == "__main__":
    main()
