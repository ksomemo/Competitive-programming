def main():
    N = int(input().strip())
    res = int(input().strip())
    if N == 1:
        return res
    for _ in range(1, N):
        t = int(input().strip())
        res = f(res, t)
    print(res)


def f(a, b):
    _gcd = gcd(a, b)
    return int(a / _gcd * b)


def gcd(a, b):
    if b == 0:
        return a
    if b == 1:
        return 1
    if b > a:
        return gcd(b, a)
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    main()
