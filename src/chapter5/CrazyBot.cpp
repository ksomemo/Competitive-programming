#include <map>

const double pointPetternCnt = 4;
double pointProb[4];
int vx[] = {1, -1, 0, 0};
int vy[] = {0, 0, -1, 1};
std::map<int, std::map<int, bool> > load;

class CrazyBot {
public:
	double getProbability(int step, int west, int east, int south, int north) {
		if (step == 1) return 1.0;

		// 進む方角が直行している場合
		if (east == 100 || west == 100 || south == 100 || north == 100) return 1.0;

		if (east >  0 && west == 0 && south >  0 && north == 0) return 1.0;
		if (east == 0 && west >  0 && south >  0 && north == 0) return 1.0;
		if (east >  0 && west == 0 && south == 0 && north >  0) return 1.0;
		if (east == 0 && west >  0 && south == 0 && north >  0) return 1.0;

		pointProb[0] = west  / 100.0;
		pointProb[1] = east  / 100.0;
		pointProb[2] = south / 100.0;
		pointProb[3] = north / 100.0;

		if (step > 2) return dfs(0, 0, step);

		double probability = 0.0;
		for (int s1p = 0; s1p < pointPetternCnt; s1p++) {
			for (int s2p = 0; s2p < pointPetternCnt; s2p++) {
				if (s1p != s2p) {
					probability += pointProb[s1p] * pointProb[s2p];
				}
			}
		}

		return probability;
	}

	double dfs(int x, int y, int restStep) {
		if (load[x][y]) return 0;
		if (restStep == 0) return 1;

		// 通過のメモをする
		load[x][y] = true;

		double probability = 0.0;
		for (int i = 0; i < pointPetternCnt; i++) {
			probability += dfs(x + vx[i], y + vy[i], restStep - 1) * pointProb[i];
		}

		// 通過のメモを消す
		load[x][y] = false;

		return probability;
	}
};

