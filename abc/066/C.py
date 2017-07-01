def main():
    N = int(input().strip())
    b = []
    for a in map(int, input().strip().split()):
        b.append(a)
        b = b[::-1]
    print(" ".join(map(str, b)))

if __name__ == '__main__':
    main()
