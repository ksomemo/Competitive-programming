def main():
    H, W = map(int, input().split())

    S = [
        input().split()
        for _ in range(H)
    ]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "snuke":
                l = [chr(o) for o in range(ord("A"), ord("Z")+1)]
                ans = l[w] + str(h+1)
                print(ans)
                return


if __name__ == '__main__':
    main()
