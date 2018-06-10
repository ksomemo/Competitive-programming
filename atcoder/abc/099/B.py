def main():
    a, b = map(int, input().split())

    xs = [0]
    for i in range(1, 999+1):
        xs.append(xs[-1] + i)

    diff = b - a
    w = xs[diff]
    ans = w - b
    print(ans)


if __name__ == '__main__':
    main()
