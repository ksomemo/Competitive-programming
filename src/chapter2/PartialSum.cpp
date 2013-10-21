class PartialSum {
public:
	bool exists(int nums[], int numCnt, int target) {
		return this->dfs(0, 0, nums, numCnt, target);
	}

	bool dfs(int nowCnt, int sum, int nums[], int numCnt, int target) {
		// 終了条件
		if (nowCnt == numCnt) return sum == target;

		// 次の数値を利用する
		if (this->dfs(nowCnt + 1, sum + nums[nowCnt], nums, numCnt, target)) {
			return true;
		}
		// 次の数値を利用しない
		if (this->dfs(nowCnt + 1, sum, nums, numCnt, target)) {
			return true;
		}

		// 見つからなかった
		return false;
	}
};

