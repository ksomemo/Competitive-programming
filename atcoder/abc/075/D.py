

def main():
    N, K = map(int, input().split())
    x, y = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    f(N, K, x, y)


def f(N, K, x, y):
    """
    制約
    * 2≦K≦N≦50
    * −10^9≦xi,yi≦10^9 (1≦i≦N)
    * xi≠xj (1≦i<j≦N)
    * yi≠yj (1≦i<j≦N)
    * 入力値はすべて整数である。(21:50 追記)

    長方形の内部にN点のうち
    K個以上の点を含みつつ、
    それぞれの辺がX軸かY軸に平行な長方形を考えます。
    →最小の面積

    制約より、
    xyの範囲を全探索はTLE
    点は重ならないかつ、50以下
    →点の座標から求めれば間に合いそう

    例題1より、
    全ての点を含む場合、
    abs(x_max-x_min) * abs(y_max-y_min)
    => 追記:
        これを分かったのに図示しなかったため、
        点が角ではなく辺上にのることに気づかず…
        点同士の組合せになってしまった(座標同士の組合せと気づけたはず)

    例題2より
    １つの場合1、ただし1*1の長方形より最大4点含む
    →この例の場合、4点から2点以上で面積1

    (x_2nd-x_min)*(y_max-y_min)
    →x_maxを除いた点が含まれる
    →50*50では済まない

    y
    ↑
    |*...
    |.*..
    |...*
    |*...
    ------→x
    (0,0)
    (0,4)
    (1,3)
    (3,1)

    各点を結んだときの面積の個数：O(N*N)
    面積求めたあとの点が含まれる個数の計算量: O(N)
    => O(N^3) => 50^3 => 1.25 * 10^5 => OK
      点を必ず含む場所からの面積
      => そこからでなくてよい, むしろ広くなる

    => 
    """
    ans = abs(max(x) - min(x)) * abs(max(y) - min(y))
    if K == N:
        print(ans)
        return

    def r(x, y):
        for _x in x:
            for _y in y:
                yield _x, _y

    # for x1, y1 in zip(x, y):
    #     for x2, y2 in zip(x, y):
    for x1, y1 in r(x, y):
        for x2, y2 in r(x, y):

            s = abs(x1-x2) * abs(y1-y2)
            if s == 0:
                continue

            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            contains_count = 0
            for x3, y3 in zip(x, y):
                if min_x <= x3 <= max_x and min_y <= y3 <= max_y:
                    contains_count += 1
            if contains_count >= K:
                ans = min(ans, s)

    print(ans)


if __name__ == "__main__":
    main()
