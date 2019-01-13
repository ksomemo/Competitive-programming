def main():
    *N, = map(int, input().split())

    if sorted(N) == sorted([1, 9, 7, 4]):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
