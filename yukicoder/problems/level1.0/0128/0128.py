def main():
    N = int(input())
    M = int(input())

    n_1000 = N // 1000
    print(n_1000 // M * 1000)

if __name__ == '__main__':
    main()
