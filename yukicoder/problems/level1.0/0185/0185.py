def main():
    N = int(input())

    s = set()
    for _ in range(N):
        x, y = map(int, input().split())
        s.add(y - x)

    if len(s) >= 2:
        print(-1)
        return

    ans = s.pop()
    if ans <= 0:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
