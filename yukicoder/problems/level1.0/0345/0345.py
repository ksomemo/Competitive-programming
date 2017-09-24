def main():
    S = input()

    length = float("inf")
    for i, c in enumerate(S):
        if c != "c":
            continue

        n_w = 0
        for j, w in enumerate(S[i + 1:], 2):
            if w == "w":
                n_w += 1
            if n_w == 2:
                length = min(length, j)
                break

    if length == float("inf"):
        print(-1)
    else:
        print(length)

if __name__ == '__main__':
    main()
