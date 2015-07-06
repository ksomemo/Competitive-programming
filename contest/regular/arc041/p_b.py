def solve(N, M, board):
    # 四隅は必ず0
    # 000    0x0
    # 0x0 => x0x
    # 000    0x0

    # x,y=>1,0, 1,1に依存する
    # x,y=>0,1, 1,1に依存する
    before = [[-1 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 四隅
            if i == 0 and j == 0: continue
            if i+1 >= N or j+1>=M: continue

            v = board[i][j]
            before[i+1][j] = v
            board[i][j] -= v
            board[i-1][j] -= v
            board[i+1][j-1] -= v
            board[i+1][j+1] -= v


    for i in range(N):
        for j in range(M):
            if before[i][j] == -1:
                before[i][j] = 0

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

if __name__ == '__main__':
    N, M = input_int_l()
    board = [input_int_l_nosep() for _ in range(N)]
    print(solve(N, M, board))
