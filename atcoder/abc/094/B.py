def main():
    N, M, X = map(int, input().split())
    A = map(int, input().split())

    costs = [0] * (N+1)
    for a in A:
        costs[a] = 1

    ans = min(sum(costs[0:X+1]), sum(costs[X:]))
    print(ans)


if __name__ == '__main__':
    main()
