def main():
    """
    0? <= h, w <= 100
        grid
    1 <= A, B <= 500

    2つの白く塗られたマス c1,c2が連結であるとは、
        マスc1からマスc2へ、
        上下左右に隣り合うマスへの移動を繰り返して、
        白く塗られたマスだけを通って移動できること

    白く塗られたマスの集合 S が連結成分であるとは、
        S のどの2 つのマスも連結である
        S に含まれないどの白く塗られたマスと、Sに含まれるどのマスも連結ではない
    """
    A, B = map(int, input().split())

    f(A, B)


def f(A, B):
    """
    解説pdfがないので、Twitter/動画を参考
    市松模様が浮かんでた
    白い海、黒い海をつくり
    白に黒の島を浮かべ、黒に白の島を浮かべるイメージらしい
    これに至る発想の流れの解説がない…発想力
        100*100だったので,最小領域で考えず最大領域を作ることはしたかった
        1マスは連結だった…
    """
    wh = "."
    bl = "#"

    grid = [
        list(wh * 50 + bl * 50)
        for _ in range(100)
    ]
    update(A, grid, wh, shift=50)
    update(B, grid, bl, shift=0)

    print(100, 100)
    for line in grid:
        print(*line, sep="")


def update(n, grid, mark, shift):
    rest = n - 1
    for i in range(0, 100, 2):
        for j in range(1+shift, shift+49, 2):
            if rest <= 0:
                return
            grid[i][j] = mark
            rest -= 1


if __name__ == '__main__':
    main()
