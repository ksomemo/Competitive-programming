def main():
    S = [input() for _ in range(12)]

    ans = sum(map(lambda s: "r" in s, S))
    print(ans)


if __name__ == '__main__':
    main()
