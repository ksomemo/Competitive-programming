#include <utility>
#include <algorithm>
class ScheduleManyWork {
public:
	int scheduleManyWork(int workCnt, int timesStart[], int timesFinish[]) {
		// pairのソートはfirst順になるので、終了時間を入れて早く終わる順にする
		std::pair<int, int> workTimes[workCnt];
		for (int i = 0; i < workCnt; i++) {
			workTimes[i].first = timesFinish[i];
			workTimes[i].second = timesStart[i];
		}
		std::sort(workTimes, workTimes + workCnt);

		int cnt = 0, finishTime = 0;
		for (int i = 0; i < workCnt; i++) {
			// 終了時間はソート済みなので、
			// 終了済みの仕事の終了時間と開始時間の整合性確認
			if (finishTime < workTimes[i].second) {
				cnt++;
				finishTime = workTimes[i].first;
			}
		}

		return cnt;
	}
};

