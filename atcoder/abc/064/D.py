def main():
    # not use N
    _ = int(input().strip())
    S = input().strip()


def no_submittion(S):
    add_S = ""
    # 追加するそれぞれの括弧の数
    n_left = 0
    n_right = 0
    # ( で始まった場合、
    # 括弧列を完成させる
    # その際、完成していない ( の個数をインクリメント
    # 完成したらデクリメント
    # 確認する
    # ) で始まった場合、( 出るまで (で埋める
    for c in S:
        if c == "(":
            if n_left == 0:
                # ( を観測した時
                add_S += "(" * n_right + ")" * n_right
                n_right = 0
            else:
                n_left -= 1
            add_S += "("
        elif c == ")":
            if n_right == 0:
                n_left += 1
            else:
                n_left -= 1


if __name__ == '__main__':
    main()
