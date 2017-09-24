#include <string>
class LakeCounting {
public:
	std::string *area;
	int col;
	int row;
	int lakeNum(std::string area[], int col, int row) {
		this->area = area;
		this->col = col;
		this->row = row;

		int num = 0;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (this->area[i][j] == 'W') {
					dfs(j, i);
					num++;
				}
			}
		}

		return num;
	}

	void dfs(int x, int y) {
		this->area[y][x] = '.';
		for (int dx = -1; dx <= 1; dx++) {
			for (int dy = -1; dy <= 1; dy++) {
				int nx = x + dx, ny = y + dy;
				if (0 <= nx && nx < this->col &&
					0 <= ny && ny < this->row &&
					this->area[ny][nx] == 'W') {

					// 周りの水溜りを置き換える
					this->dfs(nx, ny);
				}
			}
		}

		return;
	}
};

