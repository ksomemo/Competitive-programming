def solve(front, back, turn):
    if back >= turn:
        return front + turn

    # 裏返し切れなかった数を元に戻す
    return front + back - (turn - back)


if __name__ == '__main__':
    front, back = map(int, input().split())
    turn = int(input())
    print(solve(front, back, turn))
