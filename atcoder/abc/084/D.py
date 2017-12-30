def main():
    Q = int(input())
    L = []
    R = []
    n_2017_like = {
    }
    for _ in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
        r - l

    import math
    prime_nums = set([2])
    nums = list(reversed(range(3, 1 + 10 ** 5, 2)))
    while nums:
        n = nums.pop()
        if n >= math.sqrt(10 ** 5):
            break
        prime_nums.add(n)
        for x in nums:
            if x % n == 0:
                nums.remove(x)

    print(prime_nums)

if __name__ == '__main__':
    main()
