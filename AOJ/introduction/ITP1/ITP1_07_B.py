from itertools import combinations


def main():
    while True:
        n, x = map(int, input().split())
        if (n, x) == (0, 0):
            break

        ans = 0
        for nums in combinations(range(1, n + 1), 3):
            if x == sum(nums):
                ans += 1

        print(ans)


if __name__ == "__main__":
    main()
