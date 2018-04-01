def main():
    X, K = map(int, input().split())

    ans = 0
    k10 = 10 ** K
    if k10 > X:
        ans = k10
    else:
        m = X % k10
        ans = X + k10 - m

    print(ans)


def WA(X, K):
    ans = 0
    k10 = 10 ** K
    if K == 0:
        ans = X+1
    elif k10 >= X:
        ans = k10
    else:
        ans = X
        m = X % k10
        if m > 0:
            ans += k10 - m

    print(ans)

def editorial(X, K):
    t = 10 ** K
    ans = (X + t) // t * t
    print(ans)

if __name__ == '__main__':
    main()
