def main():
    s = input()
    k = int(input())

    words = (
        s[i:i+k]
        for i in range(len(s)-k+1)
    )
    ans = len(set(words))
    print(ans)


if __name__ == '__main__':
    main()
