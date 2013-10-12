#include <algorithm>

class DrawingLots {
public:
	bool existsComb(int lots[], int lotsNum, int sum) {
		// binarySearch前提のため、昇順ソートする
		int lotsCrossNum = lotsNum * lotsNum;
		int lotsCross[lotsCrossNum];

		for (int i = 0; i < lotsNum; i++) {
			for (int j = 0; j < lotsNum; j++) {
				lotsCross[lotsNum * i + j] = lots[i] + lots[j] ;
			}
		}
		std::sort(lotsCross, lotsCross + lotsCrossNum);

		for (int a = 0; a < lotsNum; a++) {
			for (int b = 0; a < lotsNum; a++) {
				if (this->binarySearch(lotsCross, lotsCrossNum, sum - lots[a] - lots[b])) {
					return true;
				}
			}
		}

		return false;
	}

	bool binarySearch(int nums[], int numsSize, int num) {
		int start = 0;
		int end = numsSize;
		for (; start + 1 <= end; ) {
			// 中央値
			int halfSize = (start + end) / 2;
			if (nums[halfSize] == num) return true;

			if (nums[halfSize] < num) {
				// 下限を上げるため
				start = halfSize + 1;
			} else if (nums[halfSize] > num) {
				// 上限を上げるため
				// halfSize - 1でない理由は、初期実行時と同じ状態を保つため
				// つまり、すでに調べた検索対象外となるhalfSizeを残す理由は、
				// numSize番目のIndexが存在しないことと同じになるため都合が良い
				end = halfSize;
			}
		}

		return false;
	}
};

