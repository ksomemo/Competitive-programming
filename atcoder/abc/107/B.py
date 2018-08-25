def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]

    ans = f(H, W, a)
    for x in ans:
        print(*x, sep="")


def f(H, W, a):
    b = []
    for line in a:
        if len(line) != line.count("."):
            b.append(line)

    if not b:
        return [[]]

    idxes = []
    for x in range(len(a[0])):
        y = sum(1 for i in range(len(b)) if b[i][x] == ".")
        if y != len(b):
            idxes.append(x)

    if not idxes:
        return [[]]

    ans = []
    for i in range(len(b)):
        line = []
        for j in range(len(a[0])):
            if j in idxes:
                line.append(b[i][j])
        ans.append(line)

    return ans


if __name__ == '__main__':
    main()
