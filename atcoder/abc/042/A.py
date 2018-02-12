def main():
    A, B, C = map(int, input().split())

    if sorted([A, B, C]) == [5, 5, 7]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
