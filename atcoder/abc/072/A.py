def main():
    X, t = map(int, input().split())
    print(max(X - t, 0))

if __name__ == '__main__':
    main()
