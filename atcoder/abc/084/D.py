import math


def main():
    Q = int(input())

    N = 10 ** 5
    is_prime = eratosthenes(N)
    like_2017 = [0 for _ in range(N + 1)]
    for i in range(3, N + 1, 2):
        if is_prime[i] and is_prime[(i + 1) // 2]:
            like_2017[i] = 1
    for i in range(3, N + 1):
        like_2017[i] += like_2017[i - 1]

    for _ in range(Q):
        l, r = map(int, input().split())
        print(like_2017[r] - like_2017[l - 1])


def eratosthenes(N):
    """エラトステネスの篩"""
    is_prime = [True for _ in range(N + 1)]
    is_prime[0] = False
    is_prime[1] = False
    max_prime = int(math.sqrt(N))
    for n in range(2, max_prime + 1):
        if is_prime[n]:
            # n-1までは判定済みのため除外されている
            # => max_prime導入も同じ理由
            for i in range(n * n, N + 1, n):
                is_prime[i] = False
    return is_prime

if __name__ == '__main__':
    main()
