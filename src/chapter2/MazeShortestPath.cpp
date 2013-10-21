#include <string>
#include <queue>
#include <utility>
#include <iostream>

class MazeShortestPath {
public:
	typedef std::pair<int, int> pos;

	int shortestTurn(std::string maze[]) {
		// 開始位置および通過ターン数の初期設定
		int sx, sy, hMax = 10, wMax = 10;
		int turn[hMax][wMax];
		std::queue<pos> que;
		for (int h = 0; h < hMax; h++) {
			for (int w = 0; w < wMax; w++) {
				turn[h][w] = -1;
				if (maze[h][w] == 'S') {
					que.push(pos(w, h));
					turn[h][w] = 0;
				}
			}
		}

		while (que.size() > 0) {
			// 移動対象
			int x = que.front().first;
			int y = que.front().second;
			que.pop();

			// ゴール判定
			if (maze[y][x] == 'G') return turn[y][x];

			// 移動予定追加
			int dx[] = {0,  0, -1, 1};
			int dy[] = {-1, 1, 0,  0};
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < wMax &&
					0 <= ny && ny < hMax &&
					turn[ny][nx] == -1 &&
					maze[ny][nx] != '#') {

					que.push(pos(nx, ny));
					turn[ny][nx] = turn[y][x] + 1;
				}
			}
		}

		return 0;
	}
};

