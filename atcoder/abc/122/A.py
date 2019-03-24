def main():
    b = input()

    if b == "A":
        ans = "T"
    elif b == "T":
        ans = "A"
    elif b == "C":
        ans = "G"
    elif b == "G":
        ans = "C"
    print(ans)


if __name__ == '__main__':
    main()
