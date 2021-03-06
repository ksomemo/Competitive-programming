def main():
    """
    1 <= K
    sunuke_K <= 10^15

    すぬけ数
        m > n
        n / S(n) <= m / S(m)

    s(n) >
    """
    K = int(input())

    answers = editorial(K)
    for ans in answers:
        print(ans)


def S(N):
    ans = 0
    while N > 0:
        N, x = divmod(N, 10)
        ans += x

    return ans


def is_snuke(m, n):
    return n * S(m) <= m * S(n)


def ex_WA(K):
    base = 1
    answers = [1]
    x = 1
    while answers[-1] < K:
        if len(str(x)) != len(str(x + base)):
            base *= 10
        x += base
        answers.append(x)

    return answers[:K]


def editorial(K):
    answers = []

    return answers


if __name__ == '__main__':
    main()
