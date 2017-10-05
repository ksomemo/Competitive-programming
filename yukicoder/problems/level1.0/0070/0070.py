def main():
    N = int(input())

    ans = 0
    for _ in range(N):
        st, end = input().split()
        st_h, st_m = map(int, st.split(":"))
        end_h, end_m = map(int, end.split(":"))

        h = end_h - st_h
        m = end_m - st_m
        if m < 0:
            # add: WA対応
            # こちらを先に処理しないと23:59睡眠の考慮漏れ
            # 0:1 0:0
            h -= 1
            m += 60
        if h < 0:
            h += 24

        ans += h * 60 + m

    print(ans)

if __name__ == '__main__':
    main()
