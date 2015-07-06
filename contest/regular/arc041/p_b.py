def solve(N, M, board):
    before = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            v = board[i][j]
            if v > 0:
                before[i+1][j] = v
                board[i][j] -= v
                board[i+2][j] -= v
                board[i+1][j-1] -= v
                board[i+1][j+1] -= v

    return before

# util
def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

def input_int_l_nosep():
    return list(map(int, list(input_str())))

def print_nested(nested, sep=''):
    for l in nested:
        print(sep.join(map(str, l)))

if __name__ == '__main__':
    N, M = input_int_l()
    board = [input_int_l_nosep() for _ in range(N)]
    print_nested(solve(N, M, board))
