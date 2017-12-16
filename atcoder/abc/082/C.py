from collections import Counter


def main():
    N = int(input())
    A = map(int, input().split())
    c = Counter(A)

    x = [
        (num, count, count - num)
        for num, count in c.items()
        if count != num
    ]

    ans = 0
    for num, count, diff in x:
        if diff > 0:
            ans += diff
        else:
            ans += count
    print(ans)

if __name__ == '__main__':
    main()
