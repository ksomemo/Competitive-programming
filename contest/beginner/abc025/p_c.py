N = 3
used = [[0 for _ in range(N)] for _ in range(N)]
last_turn = N * N

def solve(b, c):
    # もし全ての点を１人でとれるとした時の総得点
    total = sum(map(sum, b)) + sum(map(sum, c))

    # 実際の先攻の得点と総得点の差分が後攻の得点になる
    # つまり、後攻は先攻の得点が小さいほうが良い
    ans = dfs(1, b, c)
    return (ans, total - ans)

def score(used, b, c):
    ans = 0
    for i in range(N-1):
        for j in range(N):
            if used[i][j] == used[i + 1][j]:
                ans += b[i][j]

    for i in range(N):
        for j in range(N-1):
            if used[i][j] == used[i][j + 1]:
                ans += c[i][j]
    return ans

memo = {}
def dfs(turn, b, c):
    key = tuple(map(tuple, used))
    if key in memo: return memo[key]

    if turn > last_turn:
        return score(used, b, c)

    is_first_player = turn % 2 == 1
    if is_first_player:
        ans = 0
        use = 1
        comp_f = max
    else:
        ans = 9999999
        use = 2
        comp_f = min

    for i in range(N):
        for j in range(N):
            if used[i][j] != 0: continue
            # 次のターンに移行する
            # 再帰になるので、埋まるまで続く
            used[i][j] = use
            temp = dfs(turn + 1, b, c)
            ans = comp_f(temp, ans)
            # 元に戻して、別のパターンで試す
            used[i][j] = 0

    memo[key] = ans
    return ans

# templates
def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

if __name__ == "__main__":
    b = [input_int_l() for _ in range(2)] + [[0, 0, 0]]
    c = [input_int_l() + [0] for _ in range(3)]

    result = solve(b, c)
    print(result[0])
    print(result[1])
