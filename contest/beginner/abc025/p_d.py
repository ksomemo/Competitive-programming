from functools import reduce
from itertools import permutations
import operator
import copy

def extract_pos(board):
    pos_zeros = []
    for i, line in enumerate(board):
        for j, v in enumerate(line):
            if v == 0:
                pos_zeros.append((i, j))

    return pos_zeros

def fill_board(board, p, pos_zeros):
    b = copy.deepcopy(board)
    for v, pos in zip(p, pos_zeros):
        i, j = pos
        board[i][j] = v

    return b

def valid_board(borad, pos_zeros):
    for i, j in pos_zeros:
        if contain_sorted(borad, i, j):
            return False

    return True

def contain_sorted(board, i, j):
    # 横の確認
    x_min = max(i-2, 0)
    x_max = min(i, 2)
    for x in range(x_min, x_max+1):
        nums = [board[x][j], board[x+1][j], board[x+2][j]]
        sorted_nums = sorted(nums)
        if nums == sorted_nums or nums == sorted_nums[::-1]:
            return True

    # 縦の確認
    y_min = max(j-2, 0)
    y_max = min(j, 2)
    for y in range(y_min, y_max+1):
        nums = [board[i][y], board[i][y+1], board[i][y+2]]
        sorted_nums = sorted(nums)
        if nums == sorted_nums or nums == sorted_nums[::-1]:
            return True

    return False

def solve(board):
    N = len(board)
    unused_nums = set(range(1, N*N+1)) - set(reduce(operator.add, board))

    # 0の場所を把握する
    pos_zeros = extract_pos(board)

    # 残りの数で埋めてみる（全パターン）
    # 残りの数Nの階乗。。。
    cnt = 0
    for p in permutations(unused_nums):
        b = fill_board(board, p, pos_zeros)
        if valid_board(b, pos_zeros):
            cnt += 1

    return cnt % 1000000007
