def main():
    N = int(input())

    h, s = divmod(N, 3600)
    m, s = divmod(s, 60)

    ans = "{:02d}:{:02d}:{:02d}".format(h, m, s)
    print(ans)


def f(h, m, s):
    import datetime
    return datetime.time(h, m, s)

if __name__ == '__main__':
    main()
