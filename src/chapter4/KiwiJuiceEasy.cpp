using namespace std;
#include <vector>

class KiwiJuiceEasy {
public:
	vector <int> thePouring(vector <int> capacities,
							vector <int> bottles,
							vector <int> fromId, vector <int> toId) {

		unsigned int bottlesSize, capacitiesSize, fromSize, toSize;
		bottlesSize = bottles.size();
		capacitiesSize = capacities.size();
		fromSize = fromId.size();
		toSize = toId.size();

		if (bottlesSize != capacitiesSize) {
			throw "bottlesSize is not same capacitiesSize.";
		}
		if (fromSize != toSize) {
			throw "fromSize is not same toSize.";
		}

		// 分配回数
		unsigned int pouringTimes = (bottlesSize > fromSize) ? fromSize : bottlesSize;

		for (unsigned int i = 0; i < pouringTimes; i++) {
			int from = fromId[i];
			int to = toId[i];

			int diff = (bottles[from] + bottles[to] >= capacities[i])
					? capacities[i] - bottles[to]
					: bottles[from];

			bottles[from] -= diff;
			bottles[to] += diff;
		}

		return bottles;
	}
};

