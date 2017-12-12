def main():
    n = int(input())
    nums = set(range(1, 13 + 1))

    cards = {
        "S": set(),
        "H": set(),
        "C": set(),
        "D": set(),
    }
    for _ in range(n):
        mark, num = input().split()
        cards[mark].add(int(num))

    for mark in ("S", "H", "C", "D"):
        a = nums - cards[mark]
        for num in sorted(list(a)):
            print(mark, num)


if __name__ == "__main__":
    main()
