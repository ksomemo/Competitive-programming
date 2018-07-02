def main():
    N = int(input())
    *A, = map(int, input().split())

    ans = f(N, A)
    print(ans)


def f(N, A):
    ans = -float("inf")
    for i, a1 in enumerate(A):
        for j, a2 in enumerate(A):
            if i != j:
                ans = max(ans, abs(a1 - a2))

    return ans


if __name__ == '__main__':
    main()
