def main():
    X = int(input())

    for i in range(1, X+1):
        if i ** 4 == X:
            print(i)
            break


def lib(X):
    import math
    ans = int(math.sqrt(math.sqrt(X)))
    print(ans)


if __name__ == '__main__':
    main()
