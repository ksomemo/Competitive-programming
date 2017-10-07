def main():
    # WA: いついかなる時も を忘れていた
    N = int(input())

    x = [set() for _ in range(N)]
    for i in range(N):
        gs = input().split()
        for j, g in enumerate(gs):
            if i == j:
                continue
            x[j].add(g)

    nums = [
        i
        for i, _x in enumerate(x, 1)
        if "nyanpass" in _x and len(_x) == 1
    ]

    if len(nums) == 1:
        print(nums[0])
    else:
        print(-1)


def main_wa():
    N = int(input())

    number = -1
    gss = [
        input().split()
        for _ in range(N)
    ]

    for gs in gss:
        for i, g in enumerate(gs, 1):
            if g != "nyanpass":
                continue
            if number == -1:
                number = i
            elif number != i:
                print(-1)
                return

    print(number)

if __name__ == '__main__':
    main()
