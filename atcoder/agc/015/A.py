def main():
    N, A, B = map(int, input().split())

    _min = (N - 1) * A + B
    _max = (N - 1) * B + A
    ans = max(_max - _min + 1, 0)

    print(ans)

if __name__ == '__main__':
    main()
