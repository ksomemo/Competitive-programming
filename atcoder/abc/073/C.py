from collections import Counter


def main():
    N = int(input())
    counter = Counter(
        int(input())
        for _ in range(N)
    )
    answer = sum(
        1
        for v in counter.values()
        if v % 2 != 0
    )
    print(answer)

if __name__ == '__main__':
    main()
