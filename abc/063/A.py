def main():
    a, b = list(map(int, input().split()))
    answer = a + b
    if answer >= 10:
        print("error")
    else:
        print(answer)


if __name__ == '__main__':
    main()
