from itertools import permutations


def main():
    """
    荷物の少なくとも1つの面が、
    ダンボールか他の荷物のある面にぴったりとくっつくように梱包
        積んでよい
    入力例より、はみ出してはいけない
    """
    N, M, L = map(int, input().split())
    P, Q, R = map(int, input().split())

    ans = 0
    # 3!なので、べた書きでもOK
    patterns = permutations([P, Q, R])
    for i, (p, q, r) in enumerate(patterns):
        #print(i, ":", p, q, r)
        tmp = (N // p) * (M // q) * (L // r)
        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
