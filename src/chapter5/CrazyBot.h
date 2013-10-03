#include <map>

class CrazyBot {
public:
	std::map<int, std::map<int, bool> > load;
	const static double pointPetternCnt = 4;
	double pointProb[4];
	const static int vx[];
	const static int vy[];

	double getProbability(int step, int west, int east, int south, int north);

	double dfs(int x, int y, int restStep);
};

