def main():
    S = input()
    A, B, C, D = map(int, input().split())

    ans = S[:A] + '"'
    ans += S[A:B] + '"'
    ans += S[B:C] + '"'
    ans += S[C:D] + '"'
    ans += S[D:]

    print(ans)


if __name__ == '__main__':
    main()
