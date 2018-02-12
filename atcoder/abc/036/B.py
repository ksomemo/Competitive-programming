def main():
    N = int(input())
    s = [list(input()) for _ in range(N)]

    # 時計回り90度回転
    rot = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot[j][N-i-1] = s[i][j]

    for i in range(N):
        print(*rot[i], sep="")


if __name__ == '__main__':
    main()
