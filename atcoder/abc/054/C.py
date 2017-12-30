def main():
    """
    N<=8, M<=N(N-1)/2
    →全探索?
    """
    N, M = map(int, input().split())

    # 無向グラフ
    g = [
        [False] * N
        for _ in range(N)
    ]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a - 1][b - 1] = True
        g[b - 1][a - 1] = True

    # 訪問状態
    visited = [False for _ in range(N)]
    visited[0] = True

    def dfs(v, N, visited):
        if all(visited):
            return 1

        ret = 0
        for i in range(N):
            # 経路存在と訪問済み確認
            if not g[v][i] or visited[i]:
                continue

            # 再帰後に元に戻す
            visited[i] = True
            ret += dfs(i, N, visited)
            visited[i] = False

        return ret

    ans = dfs(0, N, visited)

    print(ans)

if __name__ == '__main__':
    main()
