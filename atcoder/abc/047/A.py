def main():
    a, b, c = map(int, input().split())

    s = sum([a, b, c])
    for x in (a, b, c):
        if s - x == x:
            print("Yes")
            return

    print("No")


def editorial(a, b, c):
    # maxとる/sortでよかった
    abc = sotred([a, b, c], reverse=True)

    return (
        sum(abc) == max(abc) * 2 or abc[0] == abc[1] + abc[2]
    )


if __name__ == '__main__':
    main()
