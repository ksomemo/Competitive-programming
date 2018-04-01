def main():
    N = int(input())
    A, B = zip(*[
        map(int, input().split())
        for _ in range(N)
    ])

    # 情報の中で最低点数番目までの人数と、それ未満の人数
    ans = max(A) + min(B)
    print(ans)


if __name__ == '__main__':
    main()
