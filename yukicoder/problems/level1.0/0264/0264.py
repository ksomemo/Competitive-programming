def main():
    N, K = map(int, input().split())
    # g: 0, c: 1, p: 2
    win_result = [
        (0, 1),
        (1, 2),
        (2, 0),
    ]
    if N == K:
        print("Drew")
    elif (N, K) in win_result:
        print("Won")
    else:
        print("Lost")


if __name__ == '__main__':
    main()
