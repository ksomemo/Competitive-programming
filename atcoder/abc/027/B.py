def main():
    N = int(input())
    A = list(map(int, input().split()))

    s = sum(A)
    mean, rem = divmod(s, N)
    if rem != 0:
        print(-1)
        return

    etitorial(N, A, mean)


def etitorial(N, A, mean):
    """解説より

    2つの島(left, right)に着目した時
    left側/right側それぞれに十分な人数が存在する場合、
    橋をかけずに人は調達できる
    """
    left = 0
    right = sum(A)
    ans = 0
    for i in range(1, N):
        a = A[i-1]
        left += a
        right -= a
        l_need = i * mean
        r_need = (N-i) * mean
        if left < l_need or right < r_need:
            ans += 1

    print(ans)


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
