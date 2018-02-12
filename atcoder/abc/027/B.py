def main():
    N = int(input())
    A = list(map(int, input().split()))

    s = sum(A)
    mean, rem = divmod(s, N)
    if rem != 0:
        print(-1)
        return


def WA(N, A, mean):
    bridge = {(i, i+1): False for i in range(N-1)}

    for i in range(N-1):
        a = A[i]
        d = a - mean
        if d == 0:
            pass
        elif d > 0:
            bridge[(i, i+1)] = True
            A[i] -= d
            A[i+1] += d
        elif A[i+1] >= abs(d):
            bridge[(i, i+1)] = True
            A[i] += d
            A[i+1] -= d

    for i in range(N-1, 0, -1):
        a = A[i]
        d = a - mean
        if d == 0:
            pass
        elif d > 0:
            bridge[(i-1, i)] = True
            A[i] -= d
            A[i-1] += d
        elif A[i-1] >= abs(d):
            bridge[(i-1, i)] = True
            A[i] += d
            A[i-1] -= d

    ans = sum(bridge.values())
    print(ans)


if __name__ == '__main__':
    main()
