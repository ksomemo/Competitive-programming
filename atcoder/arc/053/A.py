def main():
    H, W = map(int, input().split())

    ans = (W - 1) * H + (H - 1) * W
    print(ans)


if __name__ == '__main__':
    main()
