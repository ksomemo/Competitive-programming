class PartialSum {
public:
	bool exists(int nums[], int numCnt, int target) {
		return this->dfs(0, 0, nums, numCnt, target);
	}

	bool dfs(int nowCnt, int sum, int nums[], int numCnt, int target) {
		return true;
	}
};

