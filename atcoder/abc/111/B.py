def main():
    N = int(input())

    for i in range(N, 999+1):
        if len(set(list(str(i)))) == 1:
            print(i)
            return


if __name__ == '__main__':
    main()
