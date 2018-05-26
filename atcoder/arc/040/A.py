def main():
    N = int(input())
    S = [input() for _ in range(N)]

    t = 0
    a = 0
    for s in S:
        t += s.count("R")
        a += s.count("B")

    if t > a:
        print("TAKAHASHI")
    elif t < a:
        print("AOKI")
    else:
        print("DRAW")


if __name__ == '__main__':
    main()
