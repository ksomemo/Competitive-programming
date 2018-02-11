def main():
    N = int(input())
    S = [input() for _ in range(N)]

    votes = {}
    for name in S:
        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1

    ans = sorted(votes.items(), key=lambda x: x[1])[-1][0]

    print(ans)


if __name__ == '__main__':
    main()
