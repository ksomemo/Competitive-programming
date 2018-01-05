from collections import defaultdict, Counter


def main():
    N = int(input())
    A = map(int, input().split())

    ans = AC(N, A)
    print(ans)


def AC(N, A):
    """
    差分のとり方を用意しておく
    報告に問題があるか調べる
    差分のとり方＝組合せの要素になる
    """
    diff_dict = defaultdict(int)
    for i in range(1, N + 1):
        left, right = i - 1, N - i
        diff = abs(left - right)
        diff_dict[diff] += 1

    c = Counter(A)
    if diff_dict != c:
        return 0

    ans = 1
    for count in c.values():
        ans = (ans * count) % (10 ** 9 + 7)

    return ans

if __name__ == '__main__':
    main()
