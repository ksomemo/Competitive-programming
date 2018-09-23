def main():
    """
    """
    N, M, X, Y = map(int, input().split())
    *x, = map(int, input().split())
    *y, = map(int, input().split())

    x.append(X)
    y.append(Y)
    max_x = max(x)
    min_y = min(y)

    if max_x < min_y:
        print("No War")
    else:
        print("War")


if __name__ == '__main__':
    main()
