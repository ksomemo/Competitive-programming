def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    ans = f(N, M, S)
    # ans = TLE(N, M, S)
    print(ans)


def f(N, M, S):
    """
    PyPy3: AC
    Python3: TLE

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

    https://twitter.com/tempura_pp/status/1025823689906970624
        横方向にどれだけのばせるか
        ただし実装は楽にならない
    https://twitter.com/0214sh7/status/1025743708472324096
        ABC-018-C

    https://twitter.com/eiya5498513/status/1025744300561166337

    https://twitter.com/homesentinel214/status/1025744109389004800
    https://twitter.com/ferin_tech15/status/1025743196591030277
        掛け算して足す、累積和
        曲がる一を全探索
    https://twitter.com/satanic0258/status/1025755556823220224
        連結成分サイズを持てるUnionFind
    https://docs.google.com/document/d/11kar9MsNBbXwhfNsZdbJ17m18N8C9fdp9zE_oeZqTgU/edit

    """
    ans = 0

    import copy
    right = [[0] * M for _ in range(N)]
    left = copy.deepcopy(right)
    up = copy.deepcopy(right)
    down = copy.deepcopy(right)

    for y in range(N):
        for x in range(1, M):
            if S[y][x] == "." and S[y][x-1] == ".":
                right[y][x] += right[y][x-1] + 1

            lx = M - x - 1
            if S[y][lx] == "." and S[y][lx+1] == ".":
                left[y][lx] += left[y][lx+1] + 1

    for y in range(1, N):
        for x in range(M):
            if S[y][x] == "." and S[y-1][x] == ".":
                down[y][x] += down[y-1][x] + 1

            uy = N - y - 1
            if S[uy][x] == "." and S[uy+1][x] == ".":
                up[uy][x] += up[uy+1][x] + 1

    for y in range(N):
        for x in range(M):
            # (r * d) + (l * u) + (d * l) + (u * r)
            # r * (d + u) + l * (u + d)
            # (r + l) * (d + u)
            ans += (right[y][x] + left[y][x]) * (down[y][x] + up[y][x])

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
