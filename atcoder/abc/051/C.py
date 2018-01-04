def main():
    """
    1 秒あたり上下左右に距離 1 だけ進むことができます
    sx<tx と sy<ty を満たす点 
    (sx,sy)->(tx,ty)->(sx,sy)->(tx,ty)->(sx,sy)
    (sx,sy) と点(tx,ty) を除いて、途中で同じ座標を複数回通らないように移動しなければなりません。

    −1000≦sx<tx≦1000
    −1000≦sy<ty≦1000

    最短距離: マンハッタン距離
    to (tx,ty)N=1: 最短距離OK
    to (sx,sy)N=2: 最短距離OK
    to (tx,ty)N=3: 最短距離NG
    to (sx,sy)N=4: 最短距離NG
    """
    sx, sy, tx, ty = map(int, input().split())

    diff_x = tx - sx
    diff_y = ty - sy
    # Up -> Right
    # Down -> Left
    # Left -> Up -> Right -> Down
    # Right -> Down -> Left -> Up
    route = [
        "U" * diff_y + "R" * diff_x,
        "D" * diff_y + "L" * diff_x,
        "L" + "U" * (diff_y + 1) + "R" * (diff_x + 1) + "D",
        "R" + "D" * (diff_y + 1) + "L" * (diff_x + 1) + "U",
    ]
    for r in route:
        print(r, end="")
    print("")

if __name__ == '__main__':
    main()
