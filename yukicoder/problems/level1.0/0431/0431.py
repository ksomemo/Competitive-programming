def main():
    d1, d2, d3, S = map(int, input().split())

    if S or sum([d1, d2, d3]) < 2:
        print('SURVIVED')
    else:
        print("DEAD")

if __name__ == '__main__':
    main()
