def main():
    """
    1<=H,W<=50

    # or ## がない場合塗り方として無理
    #
    """
    H, W = map(int, input().split())

    s = [
        input()
        for _ in range(H)
    ]

    f(H, W, s)


def f(H, W, s):
    d = list(zip(
        (0, 0, 1, -1),
        (1, -1, 0, 0)
    ))
    for h in range(H):
        for w in range(W):
            if s[h][w] == ".":
                # なぜかbreakをcontinueだと思いこんでたので修正…
                continue

            ok = False
            for dy, dx in d:
                ny, nx = h+dy, w+dx
                if 0 <= ny < H and 0 <= nx < W and s[ny][nx] == "#":
                    ok = True
            if not ok:
                print("No")
                return

    print("Yes")


if __name__ == '__main__':
    main()
