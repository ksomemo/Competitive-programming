def main():
    for _ in range(3000):
        x, y = sorted(map(int, input().split()))
        if (x, y) == (0, 0):
            break
        print(x, y)

if __name__ == "__main__":
    main()
