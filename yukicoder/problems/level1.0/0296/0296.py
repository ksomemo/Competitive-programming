def main():
    N, H, M, T = map(int, input().split())

    # 2度寝、1回また寝る
    _h, _m = divmod(T * (N - 1), 60)
    add_h, m = divmod(M + _m, 60)

    # WA: 24以上考慮できていない
    print((H + _h + add_h) % 24)
    print(m)

if __name__ == '__main__':
    main()
