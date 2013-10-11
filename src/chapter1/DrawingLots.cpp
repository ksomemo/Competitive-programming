#include <algorithm>

class DrawingLots {
public:
	bool existsComb(int lots[], int lotsNum, int sum) {
		// binarySearch前提のため、昇順ソートする
		std::sort(lots, lots + lotsNum);

		for (int a = 0; a < lotsNum; a++) {
			for (int b = 0; a < lotsNum; a++) {
				for (int c = 0; a < lotsNum; a++) {
					// s = a + b + c + d;
					// s:constant
					// a~d: variable
					// d = s - a - b - c;
					// 変数が減る→ループが減る(かも！
					// 最後の比較をどうすればよいか
					// という問題にシフトした
					// a~c:index
					// これを使って数を求められる＋定数
					// 上記の足した結果になるような要素の有無
					if (this->binarySearch(lots, lotsNum, sum - lots[a] - lots[b] - lots[c])) {
						return true;
					}
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

