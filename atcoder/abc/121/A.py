def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    ans = (H-h) * (W-w)
    print(ans)


if __name__ == '__main__':
    main()
