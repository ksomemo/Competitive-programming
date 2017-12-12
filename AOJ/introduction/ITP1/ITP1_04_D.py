def main():
    n = input()
    nums = list(map(int, input().split()))
    print(min(nums), max(nums), sum(nums))

if __name__ == "__main__":
    main()
