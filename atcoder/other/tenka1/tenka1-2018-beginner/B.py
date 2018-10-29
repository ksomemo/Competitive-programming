def main():
    A, B, K = map(int, input().split())

    c = [A, B]
    for i in range(K):
        src = i % 2
        to = (i + 1) % 2

        if c[src] % 2 == 1:
            c[src] -= 1

        src_half = c[src] // 2
        c[src] -= src_half
        c[to] += src_half

    print(c[0], c[1])


if __name__ == '__main__':
    main()
