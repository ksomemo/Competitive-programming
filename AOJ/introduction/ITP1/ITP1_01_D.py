def main():
    S = int(input())
    m, s = divmod(S, 60)
    h, m = divmod(m, 60)

    print(":".join(map(str, [h, m, s])))

if __name__ == "__main__":
    main()
