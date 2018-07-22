def main():
    a1, a2, a3 = map(int, input().split())

    c1 = abs(a3 - a1) + abs(a1 - a2)
    c2 = abs(a1 - a2) + abs(a2 - a3)
    c3 = abs(a2 - a3) + abs(a3 - a1)

    ans = min([c1, c2, c3])
    print(ans)


if __name__ == '__main__':
    main()
