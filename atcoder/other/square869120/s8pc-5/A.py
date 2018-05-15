def main():
    N, T = map(int, input().split())
    *A, = map(int, input().split())

    ans = A[0]
    for a in A[1:]:
        if ans <= a:
            ans = a
        else:
            # O(1), aを無視してT倍との関係を見る
            x = ans - a
            k = (x + T - 1) // T
            ans = a + k * T
            continue

            # loop
            while ans > a:
                a += T
            ans = a

    print(ans)


if __name__ == '__main__':
    main()
