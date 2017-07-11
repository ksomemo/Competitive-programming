def main():
    N = int(input().strip())
    b = [None for _ in range(N)]

    index = N // 2
    # 追加場所
    side = -1
    if N % 2 == 0:
        side = 1

    a = map(int, input().strip().split())
    for i, a in enumerate(a):
        index = index + (side * i)
        b[index] = a
        # 追加場所の左右反転
        side *= -1
    print(" ".join(map(str, b)))

if __name__ == '__main__':
    main()
