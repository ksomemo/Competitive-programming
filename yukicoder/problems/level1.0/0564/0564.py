def main():
    H, N = map(int, input().split())
    hs = [H] + [int(input())
                for _ in range(N - 1)]
    rank = sorted(hs, reverse=True).index(H) + 1
    if rank % 10 == 1:
        print(str(rank) + "st")
    elif rank % 10 == 2:
        print(str(rank) + "nd")
    elif rank % 10 == 3:
        print(str(rank) + "rd")
    else:
        print(str(rank) + "th")

if __name__ == '__main__':
    main()
