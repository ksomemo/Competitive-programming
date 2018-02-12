def main():
    """解説より

    文字列の長さが異なる場合でも、
    2つの文字列 a, b に対し a が b より小さいことを a + b < b + a と定義し、
    それらに基づいて文字列をソートしたものを昇順に結合すれば辞書順最小を達成することができる
    """
    N, L = map(int, input().split())
    S = [input() for _ in range(N)]

    ans = ""
    for s in sorted(S):
        ans += s
    print(ans)


if __name__ == '__main__':
    main()
