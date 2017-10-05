def main():
    N = int(input())

    ok = 0
    ng = 0
    for _ in range(N):
        t, s = input().split()
        t = int(t)
        s_len = len(s)
        # 12char/1000ms
        n = min(s_len, 12 * t // 1000)
        ok += n
        ng += s_len - n

    print(ok, ng)
if __name__ == '__main__':
    main()
