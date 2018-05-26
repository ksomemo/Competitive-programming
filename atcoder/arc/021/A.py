def main():
    A = [
        list(map(int, input().split()))
        for _ in range(4)
    ]

    # 転置
    at = [b for b in zip(*A)]
    if gameover(A) and gameover(at):
        print("GAMEOVER")
    else:
        print("CONTINUE")


def gameover(A):
    for a in A:
        for i in range(3):
            if a[i] == a[i+1]:
                return False

    return True


if __name__ == '__main__':
    main()
