def main():
    L = int(input())
    N = int(input())
    W = map(int, input().split())
    ans = 0
    sum_w = 0
    for w in sorted(W):
        sum_w += w
        if sum_w > L:
            break
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
