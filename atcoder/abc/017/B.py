def main():
    """note

    正規表現での判定
    replaceで空にして最終的に空になるか
    """
    X = input()

    l = len(X)
    i = 0
    choku = True
    while i < l:
        # 被る文字がないので単純判定
        if X[i] in ("o", "k", "u"):
            i += 1
        elif X[i:i + 2] == "ch":
            i += 2
        else:
            choku = False
            break

    if choku:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
