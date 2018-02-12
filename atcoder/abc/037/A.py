def main():
    A, B, C = map(int, input().split())

    ans = C // min(A, B)
    print(ans)


if __name__ == '__main__':
    main()
