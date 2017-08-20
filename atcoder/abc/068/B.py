def main(N):
    n_div_max = 0
    answer = 1
    for n in range(1, N + 1):
        _n = n
        tmp_n_div = 0
        while True:
            _n, m = divmod(_n, 2)
            if m > 0:
                break
            tmp_n_div += 1

        if tmp_n_div >= n_div_max:
            n_div_max = tmp_n_div
            answer = max(answer, n)

    print(answer)


def main2(N):
    # 128 = 2 ** 7
    for i in reversed(range(7)):
        n = 2 ** i
        if N >= n:
            print(n)
            return

if __name__ == '__main__':
    N = int(input())
    main2(N)
