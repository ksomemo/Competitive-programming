def main():
    ABC = input()

    m = 10 ** 9 + 7
    A, B, C = map(lambda x: int(x) % m, ABC.split())

    ans = (A*B*C) % m
    print(ans)


if __name__ == '__main__':
    main()
