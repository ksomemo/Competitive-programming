def main():
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        if i % 3 == 0:
            print(i)
        elif "3" in str(i):
            print(i)

if __name__ == '__main__':
    main()
