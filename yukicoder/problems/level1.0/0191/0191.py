def main():
    N = int(input())
    C = [int(c) for c in input().split()]

    threshold = sum(C) / 10
    ans = sum(30
              for c in C
              if c <= threshold)

    print(ans)

if __name__ == '__main__':
    main()
