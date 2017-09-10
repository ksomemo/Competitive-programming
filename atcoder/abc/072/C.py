from collections import Counter


def main():
    """
    1<=N<=10^5: a_1 ... a_n
    0<=a<=10^5
    +1, -1, +0
    連続する3つの数値に対して、
    minに+1,中央に何もせず,maxに+1各操作をすると
    中央の個数が最大になる
    3つ揃わない場合もあるので、注意

    10^5で初期化 + 各数値の個数
    10^5とおりの数値についてa, a+1, a+2を想定して
        存在するものの個数をsum
    """
    N = int(input())
    counter = Counter(map(int, input().split()))
    n_max = 0

    def sort_func(t):
        return t[0]
    for a, n in sorted(counter.items(),
                       key=sort_func):

        temp_max = sum([
            counter.get(a - 1, 0),
            counter[a],
            counter.get(a + 1, 0)
        ])
        n_max = max(n_max, temp_max)
    print(n_max)

if __name__ == '__main__':
    main()
