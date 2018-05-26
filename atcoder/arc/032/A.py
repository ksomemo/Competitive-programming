def main():
    """
    n=1, s=1: prime
    n=2, s=3: prime
    n=3, s=3*4/2: not
    n=4, s=4*5/2: not -> 2以外の偶数が必ず式に含まれる
    """
    n = int(input())

    s = n * (n + 1) // 2
    if is_prime(s):
        print("WANWAN")
    else:
        print("BOWWOW")


def is_prime(n):
    if n == 1:
        return False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
