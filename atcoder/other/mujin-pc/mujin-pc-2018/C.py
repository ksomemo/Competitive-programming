def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    # ans = f(N, M, S)
    ans = TLE(N, M, S)
    print(ans)


def f(N, M, S):
    """
    順序対とは？
        ((start_n,start_m), (end_n, end_m))

    0: いずれかのマスに配置、上下左右どの向きでも良い
    1: 1マス以上進む
    2: 右90回転
    3: 1マス以上進む
    4: 置かれたマス及び停止マスには障害物はない
    5: マス目の外には出ていない

    2,3,5より
        5を満たさないパターンが存在する
        N=1 and 向き=下
        N=N and 向き=上
        M=0 and 向き=左
        M=M and 向き=右
    1,4より
        障害物マスからのスタートおよび
        障害物なしだが1マス先障害物は対象外

    順序対より、入れ替えたものもあり得る=>右に曲がれれば
    あり得る順序対を伸ばせば達成できるかが分かる
    """
    ans = 0

    return ans


def TLE(N, M, S):
    ans = 0
    # 0, 90, 180, 270
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    d = list(zip(dxs, dys))

    for _x in range(M):
        for _y in range(N):
            if S[_y][_x] == "#":
                continue
            # print(_x+1, _y+1)

            for direction, (dx, dy) in enumerate(d):
                # 方向決定して、最低限の1マス
                x = _x + dx
                y = _y + dy
                # print("\t", x+1, y+1)

                while 0 <= x < M and 0 <= y < N and S[y][x] == ".":
                    # 右90度回転して、最低限の1マス
                    new_dir = (direction + 1) % 4
                    new_dx = dxs[new_dir]
                    new_dy = dys[new_dir]
                    new_x = x + new_dx
                    new_y = y + new_dy
                    while 0 <= new_x < M and 0 <= new_y < N \
                            and S[new_y][new_x] == ".":
                        # 回転後に進めるところまで進む
                        # print("\t\t", (_x+1, _y+1), (new_x+1, new_y+1))

                        ans += 1
                        new_x += new_dx
                        new_y += new_dy

                    x += dx
                    y += dy

    return ans


if __name__ == '__main__':
    main()
