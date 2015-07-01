class ProblemC():
    def __init__(self, b, c):
        self.b = b
        self.c = c
        self.N = len(c)
        self.memo = {}

    def solve(self):
        # もし全ての点を１人でとれるとした時の総得点
        total = sum(map(sum, self.b)) + sum(map(sum, self.c))

        # 実際の先攻の得点と総得点の差分が後攻の得点になる
        # つまり、後攻は先攻の得点が小さいほうが良い
        used = [[0 for _ in range(self.N)] for _ in range(self.N)]
        score = self.dfs(1, used)
        return (score, total - score)

    def score(self, used):
        score = 0
        for i in range(self.N-1):
            for j in range(self.N):
                if used[i][j] == used[i + 1][j]:
                    score += self.b[i][j]

        for i in range(self.N):
            for j in range(self.N-1):
                if used[i][j] == used[i][j + 1]:
                    score += self.c[i][j]
        return score

    def dfs(self, turn, used):
        key = tuple(map(tuple, used))
        if key in self.memo: return self.memo[key]

        last_turn = self.N * self.N
        if turn > last_turn:
            return self.score(used)

        is_first_player = turn % 2 == 1
        if is_first_player:
            score = 0
            use = 1
            comp_f = max
        else:
            score = 9999999
            use = 2
            comp_f = min

        for i in range(self.N):
            for j in range(self.N):
                if used[i][j] != 0: continue
                # 次のターンに移行する
                # 再帰になるので、埋まるまで続く
                used[i][j] = use
                temp = self.dfs(turn + 1, used)
                score = comp_f(temp, score)
                # 元に戻して、別のパターンで試す
                used[i][j] = 0

        self.memo[key] = score
        return score

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

    result = ProblemC(b, c).solve()
    print(result[0])
    print(result[1])
