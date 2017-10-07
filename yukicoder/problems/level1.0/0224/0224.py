def main():
    n = int(input())
    S = input()
    T = input()

    ans = sum(a != b
              for a, b in zip(S, T))

    print(ans)

if __name__ == '__main__':
    main()
