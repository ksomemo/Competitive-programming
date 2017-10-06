def main():
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))

    l = [("A", A),
         ("B", B),
         ("C", C)]

    def key(pair):
        t = pair[1]
        # WA: 2個目は低いほうが優れている
        return t[0], -t[1]

    for name, _ in sorted(l,
                          key=key,
                          reverse=True):
        print(name)

if __name__ == '__main__':
    main()
