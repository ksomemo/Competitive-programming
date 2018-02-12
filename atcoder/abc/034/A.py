def main():
    x, y = map(int, input().split())

    if y > x:
        print("Better")
    else:
        print("Worse")


if __name__ == '__main__':
    main()
