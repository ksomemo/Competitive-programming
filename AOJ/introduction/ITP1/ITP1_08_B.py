def main():
    while True:
        s = input()

        if s == "0":
            break

        print(sum(map(int, list(s))))

if __name__ == "__main__":
    main()
