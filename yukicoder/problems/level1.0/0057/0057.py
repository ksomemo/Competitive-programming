def main():
    N = int(input())
    # sum(range(1, 6+1)) / 6 => 3.5
    ans = N * 3.5
    if ans % 1 == 0:
        ans = int(ans)
    print(ans)

if __name__ == '__main__':
    main()
