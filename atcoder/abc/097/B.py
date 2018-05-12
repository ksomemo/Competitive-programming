def main():
    X = int(input())

    ans = 1
    m = int(X ** 0.5)
    for i in range(1, m+1):
        for j in range(2, m+1):
            if i ** j <= X:
                ans = max(ans, i ** j)

    print(ans)


if __name__ == '__main__':
    main()
