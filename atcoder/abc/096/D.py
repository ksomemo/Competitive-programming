def main():
    """
    5 <= N <= 55
    ai is prime
    ai != aj
    sum(ai...ai5) is not prime
    """
    N = int(input())
    # f(N)


def f(N):
    max_num = 55555
    e = eratosthenes(max_num * 5)
    ps = []
    for i in range(2, max_num+1):
        if e[i]:
            ps.append(i)
    # print(len(ps)): 5637
    # TLE(N, e, ps)


def TLE(N, e, ps):
    from itertools import combinations
    for c1 in combinations(ps, N):
        c2 = list(c1)
        ok = True
        c4 = None
        for c3 in combinations(c2, 5):
            c4 = list(c3)
            # print(c4)
            if not e[sum(c4)]:
                ok = False
                break
        if ok:
            print(*c4)
            return


def eratosthenes(N):
    is_prime = [True for _ in range(N + 1)]
    is_prime[0] = False
    is_prime[1] = False
    max_prime = int(N ** 0.5)
    for n in range(2, max_prime + 1):
        if is_prime[n]:
            for i in range(n * n, N + 1, n):
                is_prime[i] = False
    return is_prime


if __name__ == '__main__':
    main()
