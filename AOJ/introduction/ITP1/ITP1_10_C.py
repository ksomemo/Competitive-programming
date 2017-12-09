import math


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        nums = list(map(int, input().split()))
        mean = sum(nums) / n
        var = sum((s - mean) ** 2 for s in nums) / n
        sd = math.sqrt(var)

        print(sd)

if __name__ == "__main__":
    main()
