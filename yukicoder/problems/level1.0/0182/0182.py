from collections import Counter


def main():
    N = int(input())
    A = map(int, input().split())

    c = Counter(A)
    ans = sum(1
              for n in c.values()
              if n == 1)

    print(ans)

if __name__ == '__main__':
    main()
