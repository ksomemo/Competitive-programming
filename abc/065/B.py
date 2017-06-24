def main():
    N = int(input().strip())
    a = [int(input().strip())
         for i in range(N)]

    b = 1
    pushed = set()
    push_count = 0
    while True:
        push_count += 1
        pushed.add(b)
        b = a[b - 1]
        if b in pushed:
            print(-1)
            break

        if b == 2:
            print(push_count)
            break

if __name__ == '__main__':
    main()
