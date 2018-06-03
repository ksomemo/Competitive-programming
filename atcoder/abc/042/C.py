def main():
    N, K = map(int, input().split())
    *D, = map(int, input().split())

    price = N
    while True:
        a = False
        for x in D:
            if str(x) in str(price):
                a = True
                break
        if not a:
            break

        price += 1

    print(price)


if __name__ == '__main__':
    main()
