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
        b[i][j] = v

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

def solve_bit_dp(board):
    max_mask = 1 << 25
    pos_zeros = []
    fix = [-1] * (25 + 1)
    dp = [0] * (max_mask)
    mo = 1000000007

    flatten = reduce(operator.add, board)
    for i, v in enumerate(flatten):
        if v == 0:
            pos_zeros.append(i)
        else:
            fix[v] = i

    dp[0] = 1
    for mask in range(max_mask - 1):
        if not dp[mask]:
            continue
        b = bin(mask).count("1") + 1
        if fix[b] >= 0:
            r = fix[b]
            y = r // 5
            x = r % 5
            if mask & (1 << r) == 0:
                if 0 < y < 4 and ((mask >> (r - 5)) ^ (mask >> (r + 5))) & 1:
                    continue
                if 0 < x < 4 and ((mask >> (r - 1)) ^ (mask >> (r + 1))) & 1:
                    continue
                dp[mask ^ (1 << r)] += dp[mask]
                if dp[mask ^ (1 << r)] >= mo:
                    dp[mask ^ (1 << r)] -= mo
        else:
            for r in pos_zeros:
                y = r // 5
                x = r % 5
                if (mask & (1 << r)) == 0:
                    if 0 < y < 4 and ((mask >> (r - 5)) ^ (mask >> (r + 5))) & 1:
                        continue
                    if 0 < x < 4 and ((mask >> (r - 1)) ^ (mask >> (r + 1))) & 1:
                        continue
                    dp[mask ^ (1 << r)] += dp[mask]
                    if dp[mask ^ (1 << r)] >= mo:
                        dp[mask ^ (1 << r)] -= mo

    return dp[(1 << 25) - 1]

# templates
def input_int_l_all(sep=None):
    import sys
    return [list(map(int, l.strip('\n').split(sep))) for l in sys.stdin]

if __name__ == "__main__":
    b = input_int_l_all()
    result = solve_bit_dp(b)
    print(result)
