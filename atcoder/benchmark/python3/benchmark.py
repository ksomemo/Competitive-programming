import sys
import time


def main():
    # 10 * 1000 * 1000
    pow = 7
    attr_pypy = "pypy_version_info"
    if hasattr(sys, attr_pypy):
        print(sys.version)
        pow = 8

    for _ in range(4, pow + 1):
        benchmark_op(10 ** _)


def benchmark_op(N):
    print("benchmark op(ms), N:{:,d}".format(N))
    a = 0

    t = time.time()
    for i in range(1, N + 1):
        pass
    print("for", "{:.10f}".format((time.time() - t) * 1000), sep='\t')

    t = time.time()
    for i in range(1, N + 1):
        a += i + 10000000
    print("add", "{:.10f}".format((time.time() - t) * 1000), sep='\t')

    t = time.time()
    for i in range(1, N + 1):
        a += i - 10000000
    print("sub", "{:.10f}".format((time.time() - t) * 1000), sep='\t')

    t = time.time()
    for i in range(1, N + 1):
        a += i * i
    print("mul", "{:.10f}".format((time.time() - t) * 1000), sep='\t')

    t = time.time()
    for i in range(1, N + 1):
        a += 10000000 / i
    print("div", "{:.10f}".format((time.time() - t) * 1000), sep='\t')

    print("")

if __name__ == '__main__':
    main()
