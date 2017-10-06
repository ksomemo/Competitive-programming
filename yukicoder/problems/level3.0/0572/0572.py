def main():
    n = int(input())
    m = int(input())

    def argmax(xs):
        return sorted(enumerate(xs),
                      key=lambda x: x[1])[-1]

    code = [
        list(map(int, input().split()))
        for _ in range(m)
    ]

    from pprint import pprint
    pprint(code)
    for c in code:
        print(argmax(c))

if __name__ == '__main__':
    main()
