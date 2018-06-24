def main():
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    ns = map(int, list(str(N)))
    s = 0
    for n in ns:
        s += n

    if N % s == 0:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    main()
