#include <algorithm>
#include <iostream>

class FenceRepair {
public:
	int lowestCostCut(int lenghs[], int lenNum) {
		std::sort(lenghs, lenghs + lenNum, std::greater<int>());

		int cost = 0;
		int sum = 0;
		for (int i = 0; i < lenNum; i++) {
			sum += lenghs[i];
		}

		// 最後の板は割る必要がない
		for (int i = 0; i < lenNum - 1; i++) {
			cost += sum;
			sum -= lenghs[i];
		}

		return cost;
	}
};

