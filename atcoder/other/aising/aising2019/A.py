def main():
    N = int(input())
    H = int(input())
    W = int(input())

    ans = (N - W + 1) * (N - H + 1)

    print(ans)


if __name__ == "__main__":
    main()
