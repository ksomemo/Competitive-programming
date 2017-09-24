#include <algorithm>
#include <iostream>

class FenceRepair {
public:
	int lowestCostCut(int lenghs[], int lenNum) {
		// 最小のコスト2つが最後にかかるコストになる
		// つまり、その2つの板の長をを足し、新しい板で置き換えると、
		// 最後の分割の前の状態を再現できる
		// この状態から最小のコスト2つの板を選んで繰り返せばよい

		// 最後の板は割る必要がないので、分割したい個数-1
		int cost = 0;
		for (int i = 0; i < lenNum - 1; i++) {
			// 最小分割から計算するボトムアップにするため、ソートする
			std::sort(lenghs, lenghs + lenNum);

			cost += lenghs[i] + lenghs[i + 1];
			lenghs[i + 1] += lenghs[i];
		}

		return cost;
	}
};

