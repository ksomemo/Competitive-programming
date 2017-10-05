def main():
    N = int(input())

    yes_nums = set(range(9 + 1))
    no_nums = set()
    for _ in range(N):
        x = input().split()
        nums = map(int, x[:-1])
        if x[-1] == "YES":
            yes_nums &= set(nums)
        else:
            no_nums.update(nums)

    fixed = yes_nums - no_nums
    print(fixed.pop())

if __name__ == '__main__':
    main()
