def main():
    A, B = map(int, input().split())

    ans = (A + B) % 24
    print(ans)

if __name__ == '__main__':
    main()
