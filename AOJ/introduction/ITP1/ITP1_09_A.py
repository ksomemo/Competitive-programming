def main():
    W = input().lower()
    words = []
    while True:
        T = input()
        if T == "END_OF_TEXT":
            break

        words.extend(T.split(" "))

    ans = sum(1 for word in words if word.lower() == W)

    print(ans)

if __name__ == "__main__":
    main()
