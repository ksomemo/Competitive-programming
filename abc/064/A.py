def main():
    r, g, b = list(map(int, input().strip().split()))
    v = r * 100 + g * 10 + b
    if v % 4 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
