def main():
    N = int(input())
    S = [input() for i in range(N)]
    T = input()

    S1 = [s.replace("?", "z") for s in S]
    S2 = [s.replace("?", "a") for s in S]
    S1.append(T)
    S2.append(T)

    idx1 = sorted(S1).index(T)
    idx2 = (N+1) - 1 - sorted(S2, reverse=True).index(T)

    ans = range(idx1+1, idx2+1+1)
    print(*ans)


if __name__ == '__main__':
    main()
