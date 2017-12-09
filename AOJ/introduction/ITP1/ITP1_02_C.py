def main():
    nums = map(int, input().split())
    sorted_nums = sorted(nums)
    print(" ".join(map(str, sorted_nums)))

if __name__ == "__main__":
    main()
