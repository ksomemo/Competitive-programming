def main():
    A = int(input())
    B = int(input())
    C = int(input())

    l = [("A", A), ("B", B), ("C", C)]
    for name, _ in sorted(l,
                          key=lambda x: x[1],
                          reverse=True):
        print(name)

if __name__ == '__main__':
    main()
