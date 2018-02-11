def main():
    C = [
        input().split()
        for _ in range(4)
    ]

    for i in range(3, -1, -1):
        print(" ".join(C[i][::-1]))


if __name__ == '__main__':
    main()
