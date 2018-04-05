def main():
    A, B, C = map(int, input().split())

    def d(A, B, C):
        """
        どれか偶数なら半分にできる
            if A%2==0 or B%2==0 or C%2==0:
        どれも奇数なら e.g. A = 3 + (2 + 1) のとき
        厚さ1の面ができるのでそれが差分
        """
        return (A - A // 2 * 2) * B * C

    ans = min([
        d(A, B, C),
        d(B, A, C),
        d(C, A, B)
    ])
    print(ans)


if __name__ == '__main__':
    main()
