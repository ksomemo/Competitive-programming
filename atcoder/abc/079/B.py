def main():
    N = int(input())

    print(f(N))


def f(N):
    a, b = 2, 1
    for i in range(2, N + 1):
        a, b = b, a + b

    return b

if __name__ == '__main__':
    main()
