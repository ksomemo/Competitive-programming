def solve(front, back, turn):
    if back >= turn:
        return front + turn

    # 裏返し切れなかった数を元に戻す
    return front + back - (turn - back)
