#include <vector>

class TriangleMaxPerimeter {
public:
	std::vector<int> sidesMaximizedPerimeter(std::vector<int> inputSides) {
		std::vector<int> sides;
		sides.push_back(0);
		sides.push_back(0);
		sides.push_back(0);
		int sidesNum = inputSides.size();

		if (sidesNum < 3) return sides;

		int maxPerimeter = 0;
		for (int i = 0; i < sidesNum; i++) {
			for (int j = 0; j < sidesNum; j++) {
				if (j == i) continue;
				for (int k = 0; k < sidesNum; k++) {
					if (k == j || k == i) continue;

					int perimeter = inputSides[i] + inputSides[j] + inputSides[k];
					int tmpIndex = inputSides[i] >= inputSides[j] ? i : j;
					int longestSide = inputSides[tmpIndex] >= inputSides[k]
										? inputSides[tmpIndex]
										: inputSides[k];

					if (longestSide >= (perimeter - longestSide)) continue;

					if (perimeter > maxPerimeter) {
						perimeter = maxPerimeter;
						sides[0] = inputSides[i];
						sides[1] = inputSides[j];
						sides[2] = inputSides[k];
					}
				}
			}
		}

		return sides;
	}
};

