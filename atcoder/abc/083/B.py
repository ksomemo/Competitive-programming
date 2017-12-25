def main():
    """
    1 以上 N 以下の整数のうち、
    10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
    """
    N, A, B = map(int, input().split())

    ans = 0
    for n in range(1, N + 1):
        s = sum(map(int, str(n)))
        if A <= s <= B:
            ans += n

    print(ans)

if __name__ == '__main__':
    main()
