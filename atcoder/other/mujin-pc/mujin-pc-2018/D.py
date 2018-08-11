def main():
    N, M = map(int, input().split())

    # ans = f(N, M)
    ans = my_func(N, M)
    print(ans)


def rev(x):
    return int(str(x)[::-1])


def test_rev():
    x_ans = [
        (123, 321),
        (90, 9),
        (5, 5)
    ]
    for x, ans in x_ans:
        assert rev(x) == ans


def operate(x, y):
    if x < y:
        x = rev(x)
    else:
        y = rev(y)

    if x < y:
        y -= x
    else:
        x -= y

    return x, y


def my_func(N, M):
    """
    再帰ではなく、メモ化のような状態管理をした
    ペアの確保数が多くなるとMLEになりそう
    +状態が多いと処理できない・管理が難しいと思うので、
    DFSでペアを関数呼び出しのスタックに任せ、状態管理をシンプルにして対処がよさそう

    dfs
        https://beta.atcoder.jp/contests/mujin-pc-2018/submissions/2949403
        https://beta.atcoder.jp/contests/mujin-pc-2018/submissions/2944702
    """
    UNKNOWN = 0
    INF_LOOP = 1
    STOP = 2
    CHECKING = 3

    t = [[UNKNOWN] * 1000 for _ in range(1000)]
    for i in range(N):
        t[i][0] = STOP
    for i in range(M):
        t[0][i] = STOP

    for _y in range(1, N+1):
        for _x in range(1, M+1):
            # print(_x,  _y)
            pair = []
            is_loop = False
            x, y = _x, _y
            while x > 0 and y > 0:
                pair.append((y, x))
                status = t[y][x]
                if status in (INF_LOOP, CHECKING):
                    is_loop = True
                    break
                elif status == STOP:
                    break
                else:
                    t[y][x] = CHECKING

                x, y = operate(x, y)

            # print("", status, (x, y), pair, sep="\t")
            if is_loop:
                status = INF_LOOP
            else:
                status = STOP
            for y, x in pair:
                t[y][x] = status

    ans = 0
    for row in t[:N+1]:
        for status in row[:M+1]:
            if status == INF_LOOP:
                ans += 1

    return ans


def f(N, M):
    """
    1 <= N, M <= 999

    1: x,y のいずれかが 0なら、終了する
    2: x < y なら
        x を rev(x) で、
        そうでないなら y を rev(y) で置き換える。
    3: 上の操作後、x<y となっていれば
        y を y−xで、
        そうでなければ x を x−yで置き換える。

    https://beta.atcoder.jp/contests/mujin-pc-2018/submissions/2946826

    https://twitter.com/armeria_betrue/status/1025744661627920385
        Snuke Mumbers

    https://twitter.com/259_Momone/status/1025745867238662145

    https://twitter.com/homesentinel214/status/1025744109389004800
        Union Find

    https://twitter.com/hamko_intel/status/1025780855468257281
        全遷移の逆辺を張って、0から到達可能な頂点を数え上げ
        https://mujin-pc-2018.contest.atcoder.jp/submissions/2943150

    https://twitter.com/hamko_intel/status/1025782989505015809
    https://docs.google.com/document/d/1dPEhrnvd8Qn64LDQ5tzNoOjdDj07gyjn223rYy-m0Qk/edit
        ループ検出
            有向グラフの閉路検出
            https://mujin-pc-2018.contest.atcoder.jp/submissions/2943393
            実装が難しい？バグを避ける強連結成分分解が楽
    """
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            s = set()
            # print(i, j)
            x, y = i, j
            while True:
                # print("\t", x, y)
                # 無限ループ判定
                if (x, y) in s:
                    ans += 1
                    break

                s.add((x, y))
                if x == 0 or y == 0:
                    break

                if x < y:
                    x = rev(x)
                else:
                    y = rev(y)

                if x < y:
                    y -= x
                else:
                    x -= y

    return ans


if __name__ == '__main__':
    main()
