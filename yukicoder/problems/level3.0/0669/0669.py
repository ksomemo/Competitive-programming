def main():
    """
    酒の種類:      1 ≤ N ≤ 1000000 
    一度に飲める量: 1 ≤ K ≤ 1000
    各種類の酒の量: 0 ≤ Ai≤ 1000000

    先手で勝てるか？(酒の残りがなく、飲めなくなったら負け)
    石取りゲームと同じ？

    解説: Nim, Grundy数
        Nimにおいて取れる石の数が1～Kとなったバージョンの問題である。
        以下、Nimの言葉で書く。
        Grundy数は各山のGrundy数全てのxorである。
        各山のGrundy数は（石の個数）%（K+1）である。
        この事は帰納法で簡単に示せる。後は実装するだけ。

        https://yukicoder.me/problems/no/669/editorial
        http://yang33-kassa.hatenablog.com/entry/2017/12/21/202812

    ニコ生コメント
        各山の個数をmod(K+1)したゲームの必勝側は、
        各山のmod(K+1)を不変に保てるので、結局ただのNimになる、と考えると簡単
        先手が必ずxor 0 で後手に渡せるから勝てる

        各山の個数をmod(K+1)したゲームの必勝側は、
        各山のmod(K+1)を不変に保てるので、結局普通のNimになる、と考えると簡単

        石取りゲームの必勝法 ～ 二進法と XOR ～: 秋葉さんの解説動画
        https://www.youtube.com/watch?v=DfR0vQZoa1Y
    """
    N,K  = map(int,input().split())
    *A,  = map(int,input().split())

    ans = "YES"
    print(ans)

if __name__ == '__main__':
    main()
