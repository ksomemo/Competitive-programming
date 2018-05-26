def main():
    N, L = map(int, input().split())
    S = input()

    t = 1
    ans = 0
    for op in list(S):
        if op == "+":
            t += 1
        else:
            t -= 1

        if t > L:
            t = 1
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
