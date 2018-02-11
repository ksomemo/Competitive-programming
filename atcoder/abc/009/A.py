def main():
    N = int(input())

    d, m = divmod(N, 2)

    print(d + m)

if __name__ == '__main__':
    main()
