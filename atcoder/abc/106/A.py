def main():
    A, B = map(int, input().split())

    # ans = AC(A, B)
    ans = editorial(A, B)
    print(ans)


def AC(A, B):
    ans = (A - 1) * (B - 1)
    return ans


def editorial(A, B):
    return A * B - A - B + 1


if __name__ == '__main__':
    main()
