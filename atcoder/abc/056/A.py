def main():
    a, b = input().split()

    pattern = {
        ("H", "H"): "H",
        ("H", "D"): "D",
        ("D", "H"): "D",
        ("D", "D"): "H",
    }
    ans = pattern[(a, b)]
    print(ans)

if __name__ == '__main__':
    main()
