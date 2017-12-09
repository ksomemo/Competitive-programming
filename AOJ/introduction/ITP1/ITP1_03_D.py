def main():
    a, b, c = map(int, input().split())

    ans = 0
    for i in range(a, b + 1):
        d = c % i
        if d == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
