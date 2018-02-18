from collections import deque


def main():
    """
    ゲームの開始時点ではマス (1,1)
    上下左右の 4 方向のいずれかに 1 マスだけ動かすことを繰り返す
    白いマスだけを通って (H,W) にたどり着けばゲームクリア

    マス (i,j) 最初
    白で塗られている場合 .
    黒で塗られている場合 #

    いくつかの白いマス目の色を黒に変えることができる
    ただし, マス (1,1) と (H,W) の色を変えることはできず
    -> ルートの変更は不可能

    ゲームをクリアしたとき, ゲームの開始前にマスの色を変えた回数がすぬけ君のスコアとなる
    最大のスコアを求めなさい
    → 最短距離を求め,必要ない白マスを黒に変えれば高スコア(BFS?)
    → 経路を覚えておかないといけない
    """
    H, W = map(int, input().split())
    S = [
        input()
        for _ in range(H)
    ]

    bfs(S, H, W)


def bfs(S, H, W):
    # 距離を追加, 経路情報は必要ない
    q = deque([(0, 0, 0)])
    visited = [
        [False] * W
        for _ in range(H)
    ]
    visited[0][0] = True

    goal = False
    dist = 0
    while q:
        x, y, dist = q.popleft()
        if (x, y) == (W-1, H-1):
            goal = True
            break

        for dx in (-1, 1):
            nx = x+dx
            if 0 <= nx < W:
                if S[y][nx] == "." and not visited[y][nx]:
                    # ここで訪問済みにしないとTLE
                    q.append((nx, y, dist+1))
                    visited[y][nx] = True
        for dy in (-1, 1):
            ny = y+dy
            if 0 <= ny < H:
                if S[ny][x] == "." and not visited[ny][x]:
                    q.append((x, ny, dist+1))
                    visited[ny][x] = True

    if goal:
        w_count = 0
        for s in S:
            w_count += s.count(".")
        # startは通ってないので距離に含まれない
        print(w_count - dist - 1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
