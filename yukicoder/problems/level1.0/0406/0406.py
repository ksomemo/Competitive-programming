def main():
    N = int(input())
    xs = map(int, input().split())
    xs = list(sorted(xs))

    if len(xs) != len(set(xs)):
        print("NO")
        return

    pairs = zip(xs[:-1], xs[1:])
    if len(set(abs(x1 - x2)
               for x1, x2 in pairs)) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
