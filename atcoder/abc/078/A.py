def main():
    X, Y = input().split()

    if X < Y:
        print("<")
    elif X == Y:
        print("=")
    else:
        print(">")

if __name__ == '__main__':
    main()
