def main():
    S = map(int, input().split())

    trimmed = sorted(S)[1:-1]
    trimmed_mean = sum(trimmed) / len(trimmed)
    print("{:.2f}".format(trimmed_mean))

if __name__ == '__main__':
    main()
