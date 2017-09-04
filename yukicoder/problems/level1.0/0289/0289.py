def main():
    S = input()
    _sum = sum(int(c) for c in S if c.isdigit())
    print(_sum)

if __name__ == '__main__':
    main()
