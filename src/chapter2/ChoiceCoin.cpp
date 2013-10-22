#include <algorithm>

class ChoiceCoin {
public:
	int choiceFewCoins(int charge, int coinTypeNums, int coinTypes[], int coinNums[]) {

		// 少ない数で払うために高い硬貨から使う
		int totalUseNum = 0;
		for (int i = coinTypeNums; i > 0; i--) {
			// 持っている数と料金を基準とした使える硬貨の最大数
			int useNum = std::min(coinNums[i - 1], charge / coinTypes[i - 1]);
			charge -= useNum * coinTypes[i - 1];
			totalUseNum += useNum;
		}

		return totalUseNum;
	}
};

