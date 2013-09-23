using namespace std;
#include <vector>

class KiwiJuiceEasy {
public:
	vector <int> thePouring(vector <int> capacities,
							vector <int> bottles,
							vector <int> fromId, vector <int> toId) {

		for (int i = 0; i < bottles.size(); i++) {
			int from = fromId[i];
			int to = toId[i];

			if (bottles[from] + bottles[to] >= capacities[i]) {
				int diff = capacities[i] - bottles[to];
				bottles[from] -= diff;
				bottles[to] += diff;

			} else {
				bottles[to] += bottles[from];
				bottles[from] = 0;
			}
		}

		return bottles;
	}
};

