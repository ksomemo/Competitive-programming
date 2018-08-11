def main():
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    for f in range(25+1):
        for s in range(14+1):
            if (f * 4 + s * 7) == N:
                return "Yes"

    return "No"


if __name__ == '__main__':
    main()
