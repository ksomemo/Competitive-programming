def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split()))
          for _ in range(M)]

    ans = f(N, M, AB)
    ans = editorial(N, M, AB)
    print(ans)


def f(N, M, AB):
    """
    """
    ans = 0
    return ans


def editorial(N, M, AB):
    ans = 0
    return ans


if __name__ == "__main__":
    main()
