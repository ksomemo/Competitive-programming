def main():
    a = int(input())
    b = int(input())

    # d1がよい: (a,b)=(9,8)
    # d2がよい: (a,b)=(0,9)
    # => (10+a,b) = (10,9)
    # d3がよい: (a,b)=(9,0)
    # => (a,10+b) = (9,10)
    d1 = abs(a - b)
    d2 = 10 + a - b
    d3 = 10 + b - a

    ans = min([d1, d2, d3])
    print(ans)


if __name__ == '__main__':
    main()
