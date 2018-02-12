def main():
    a, b, c, d = map(int, input().split())
    t, aoki = b/a, d/c
    if t > aoki:
        print('TAKAHASHI')
    elif t == aoki:
        print('DRAW')
    else:
        print('AOKI')


if __name__ == '__main__':
    main()
