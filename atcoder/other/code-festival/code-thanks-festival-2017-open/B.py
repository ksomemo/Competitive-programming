def main():
    """
    a: yes
    ab: not, + a
        bを基準にして左右を1文字ずつ比較: 0
    abc: not, +ba
        cを基準: 0
        bを基準: 0
        半分切り上げまで
    abcb: not, + a
        bを基準: 0
        cを基準: 1 (bとb) ->残りの1文字追加
    """
    S = input()

    # editorial(S)
    simple_AC(S)


def simple_AC(S):
    for i in range(len(S)):
        ST = S + S[:i][::-1]
        if ST == ST[::-1]:
            print(i)
            return


def editorial(S):
    """
    追加文字はなんでもよい
    |S|-1で解けることがわかっているので、その長さ未満まで試す
    """
    ls = len(S)
    ans = ls - 1
    for i in range(ls):
        ST = S + ("*" * i)
        same = 0
        for c1, c2 in zip(ST, ST[::-1]):
            if c1 == c2 or "*" in (c1, c2):
                same += 1
        if same == ls + i:
            print(i)
            return

    print(ans)


def WA(S):
    # 先頭追加はできず末尾追記より、逆順で考え真ん中まで
    # 一番末尾を中心とした時、末尾に長さ-1文字追加すれば必ず可能
    S_rev = S[::-1]
    l = len(S)
    ans = l - 1
    mid = (l + 1) // 2
    for i in range(1, mid):
        left_rev = S_rev[:i][::-1]
        right = S_rev[i+1:]

        # 中心からどこまで一致するか
        same_count = 0
        for c1, c2 in zip(left_rev, right):
            if c1 == c2:
                same_count += 1
            else:
                break

        # 中途半端な一致は文字を追加できない
        ls = [len(left_rev), len(right)]
        l_min, l_max = min(ls), max(ls)
        if same_count == l_min:
            ans = min(ans, l_max - l_min)

        # print(i, left, S_rev[i], right)

    print(ans)


if __name__ == '__main__':
    main()
