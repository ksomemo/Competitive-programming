def main():
    N = int(input())
    S = input().split()
    T = input().split()
    for i, (s, t) in enumerate(zip(S, T), 1):
        if s != t:
            print(i)
            print(s)
            print(t)
            break

if __name__ == '__main__':
    main()
