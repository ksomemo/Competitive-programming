def main():
    N = int(input())
    d, m = divmod(N, 10)

    if m*15 > 100:
        ans = (d+1)*100
    else:
        ans = d*100+m*15

    print(ans)


if __name__ == '__main__':
    main()
