def main():
    """
    はじめ、好きな単語を発言する
    以降、次の条件を満たす単語を発言することを繰り返す
        その単語はまだ発言していない単語である
        その単語の先頭の文字は直前に発言した単語の末尾の文字と一致する
    """
    N = int(input())
    W = [input() for _ in range(N)]

    ans = AC(N, W)
    print(ans)


def AC(N, W):
    for i, w in enumerate(W[1:]):
        if W.count(w) >= 2:
            return "No"

        if W[i][-1] != w[0]:
            return "No"

    return "Yes"


if __name__ == '__main__':
    main()
