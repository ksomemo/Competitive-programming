def main():
    N = int(input())

    ans = 1
    for _ in range(N):
        ans *= 10
    ans += 7

    ans_s = "1" + "0" * (N - 1) + "7"
    assert str(ans) == ans_s
    assert ans == 10 ** N + 7

    print(ans)


if __name__ == '__main__':
    main()
