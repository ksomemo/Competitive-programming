def main():
    """
    うしろから確定させる
    """
    N = int(input())
    AB = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans = 0
    for a, b in AB[::-1]:
        c = (a + ans) % b
        #if a + ans > b and c == 0:
        if c == 0:
            pass
        else:
            d = b - c
            #print(d)
            ans += d

    print(ans)

if __name__ == '__main__':
    main()
