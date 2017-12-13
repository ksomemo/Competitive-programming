def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = map(int, input().split())

    ans = 0
    for t in T:
        if binsearch(t, S):
            ans += 1

    print(ans)


def binsearch(x, xs):
    left = 0
    right = len(xs)
    mid = (left + right) // 2

    while left < right:
        if x == xs[mid]:
            return True
        elif x < xs[mid]:
            right = mid
        else:
            # ずらさないとループ
            # e.g. (2 + 3) // 2 -> 2
            # l:2, m:2, r:3
            left = mid + 1
        mid = (left + right) // 2

    return False

if __name__ == '__main__':
    main()
