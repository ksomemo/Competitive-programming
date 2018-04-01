import string


def main():
    """
    abcdefghijklmnopqrstuvwxyz
    zyxwvutsrqponmlkjihgfedcba
    """
    S = input()

    az = string.ascii_lowercase
    za = az[::-1]
    if len(S) < len(az):
        # 全文字使ってない
        s_s = set(S)
        s_az = set(az)
        a = sorted(list(s_az - s_s))[0]

        # S=abのとき、abc < ac==True なので追加で良い
        ans = S + a
        print(ans)
        return

    WA(S, az, za)

def WA(S, az, za):
    # 全文字使ってsort済み
    if S == az or S == za:
        print(-1)
        return

    for i in range(1, len(S) + 1):
        # sort済みかつ連続であるか
        # if S[:i] == az[:i]:
        if S[:i] == az[:i] or S[:i] == za[:i]:
            continue

        rev = 1
        if S[:i-1] == az[:i-1]:
            rev = 0
        # sortずみでないので、sort済みまでの最後を置き換え
        if S[i:]:
            a = sorted(S[i:])[0]
            ans = S[:i-2+rev] + a
            print(ans)
            return
        else:
            print(-1)
            return

if __name__ == '__main__':
    main()
