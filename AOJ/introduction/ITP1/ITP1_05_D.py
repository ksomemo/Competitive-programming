def main():
    n = int(input())
    for i in range(1, n + 1):
        x = i
        if x % 3 == 0:
            print("", i, end="")
            continue

        while x > 0:
            if x % 10 == 3:
                print("", i, end="")
                break

            x //= 10

    print("")

if __name__ == "__main__":
    main()
