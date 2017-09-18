from datetime import datetime as dt


def main():
    # 10 * 1000 * 1000
    for _ in range(4, 7 + 1):
        benchmark_op(10 ** _)


def benchmark_op(N):
    print("benchmark op(ms), N:{:,d}".format(N))
    a = 0

    d = dt.now()
    for i in range(1, N + 1):
        pass
    print("for", (dt.now() - d).microseconds / 1000)

    d = dt.now()
    for i in range(1, N + 1):
        a += i + 10000000
    print("add", (dt.now() - d).microseconds / 1000)

    d = dt.now()
    for i in range(1, N + 1):
        a += i - 10000000
    print("sub", (dt.now() - d).microseconds / 1000)

    d = dt.now()
    for i in range(1, N + 1):
        a += i * i
    print("mul", (dt.now() - d).microseconds / 1000)

    d = dt.now()
    for i in range(1, N + 1):
        a += 10000000 / i
    print("div", (dt.now() - d).microseconds / 1000)

    print("")

if __name__ == '__main__':
    main()
