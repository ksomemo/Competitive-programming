def main():
    S = input()
    for i, c in enumerate(S, 1):
        # i右ずらしなので、戻す分を計算
        rot = i % 26
        # Aを基準にどれだけずれているか
        a_rot = (ord(c) - ord("A"))
        b = (a_rot - rot) % 26
        print(chr(ord("A") + b), end="")

    print("")

if __name__ == '__main__':
    main()
