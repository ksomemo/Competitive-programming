#include <map>
#include "CrazyBot.h"

const int CrazyBot::vx[] = {1, -1, 0, 0};
const int CrazyBot::vy[] = {0, 0, -1, 1};

double CrazyBot::getProbability(int step, int west, int east, int south, int north) {
	pointProb[0] = west  / 100.0;
	pointProb[1] = east  / 100.0;
	pointProb[2] = south / 100.0;
	pointProb[3] = north / 100.0;

	return dfs(0, 0, step);
}

double CrazyBot::dfs(int x, int y, int restStep) {
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

