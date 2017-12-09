def main():
    a, b = map(int, input().split())
    if a > b:
        symbol = ">"
    elif a < b:
        symbol = "<"
    else:
        symbol = "=="

    print("a " + symbol + " b")

if __name__ == "__main__":
    main()
