def main():
    N = int(input())
    ps = [int(input()) for _ in range(N)]

    ans = min(f(p) for p in ps)
    print(ans)


def f(p):
    ans = 0
    while p >= 10:
        d, m = divmod(p, 10)
        if m == 0:
            ans += 1
            p = d
        else:
            break

    return ans


if __name__ == '__main__':
    main()
