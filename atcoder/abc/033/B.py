def main():
    N = int(input())
    sp = []
    sum_p = 0
    for _ in range(N):
        s, p = input().split()
        p = int(p)
        sp.append((s, p))

        sum_p += p

    sp = sorted(sp, key=lambda x: x[1])
    # 過半数
    majority = sum_p // 2 + 1
    if sp[-1][1] >= majority:
        print(sp[-1][0])
    else:
        print("atcoder")


if __name__ == '__main__':
    main()
