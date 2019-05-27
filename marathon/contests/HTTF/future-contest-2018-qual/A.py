import random
import copy
import time


def main():
    Main().solve()


class Main:

    def __init__(self, seed=20180217):
        # 制約
        self.N = 100
        self.row = 100
        self.col = 100
        self.pnum = 1000
        self.ans = [[None] * 3 for _ in range(1000)]
        self.map = [[None] * 3 for _ in range(1000)]
        self.seed = seed
        # 山の外周に沿って斜め移動
        self.dx = [1, -1, -1, 1]
        self.dy = [1, 1, -1, -1]
        # 時間制限: 6sec / メモリ制限: 1024MB
        self.time_limit = 5500
        self.time_limit = 2000

    def solve(self):
        self.input()
        self.init(self.seed)
        self.simulate()
        # self.output_0()
        self.output()

    def input(self):
        self.map = [] * self.row
        for _ in range(self.row):
            *row, = map(int, input().split())
            self.map.append(row)

    def output_0(self):
        """ACを取る"""
        print(0)

    def init(self, seed=None):
        random.seed(seed)
        for i in range(self.pnum):
            # [0, 100)
            # x = rnd.nextInt(100)
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            h = random.randint(0, 99) + 1
            self.ans[i] = [x, y, h]

    def output(self):
        """乱択した山を出力する"""
        print(len(self.ans))
        for x, y, h in self.ans:
            print(x, y, h)

    def simulate(self):
        """シミュレーション

        ちゃんとシミュレータ作ってスコア計算し、 制限時間いっぱい1,000個のランダムな山を生成して、 一番良かったものを出力
        """
        # TLE 対策
        st = time.time() * 1000
        et = st + self.time_limit

        # いったん評価
        best_score = self.eval(self.ans)
        *best_output, = range(1000)
        for i, out in enumerate(self.ans):
            #best_output[i] = out.copy()
            best_output[i] = out[:]

        while time.time() * 1000 < et:
            # 乱数生成して評価用データ作成
            tmp_output = [None] * len(best_output)
            for i in range(self.pnum):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
                h = random.randint(0, 99) + 1
                tmp_output[i] = [x, y, h]

            # 再度評価して更新
            tmp_score = self.eval(tmp_output)
            if best_score > tmp_score:
                best_output = tmp_output
                for out in best_output:
                    best_output[i] = out[:]

        # 反映
        for i, out in enumerate(best_output):
            self.ans[i] = out[:]

    # def eval(self, output) -> int:
    def eval(self, output):
        """評価値の算出"""
        ret = 0
        ans_map = copy.deepcopy(self.map)

        for out in output:
            x, y, h = out
            ans_map[x][y] += h
            for plus in range(1, h):
                d = h - plus
                x = out[0]
                y = out[1] - d
                # 四方
                for _dx, _dy in zip(self.dx, self.dy):
                    # 移動距離
                    for _ in range(d):
                        x = x + _dx
                        y = y + _dy
                        if self.out_map(x, y):
                            continue
                        ans_map[x][y] += plus

        for i in range(self.row):
            for j in range(self.col):
                ret += abs(self.map[i][j] - ans_map[i][j])

        return ret

    # def in_map(self, x: int, y: int) -> bool:
    def in_map(self, x, y):
        in_x = 0 <= x and x < self.row
        in_y = 0 <= y and y < self.col
        return in_x and in_y

    # def out_map(self, x: int, y: int) -> bool:
    def out_map(self, x, y):
        return not self.in_map(x, y)


if __name__ == "__main__":
    main()
