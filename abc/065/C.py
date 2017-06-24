import math


def main():
    N, M = list(map(int, input().strip().split()))
    diff = abs(N - M)
    if diff > 1:
        print(0)
        return

    n_fact = math.factorial(N)
    m_fact = math.factorial(M)
    a = n_fact * m_fact
    if diff == 0:
        a = a * 2

    print(a % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
