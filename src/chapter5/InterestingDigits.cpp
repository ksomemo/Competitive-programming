#include <vector>

class InterestingDigits {
public:
	std::vector <int> digits(int base) {
		std::vector <int> digits;

		// 4桁以上は考慮しない
		for (int n = 2; n < base; n++) {
			bool isRegularity = true;
			for (int d1 = 0; d1 < base; d1++) {
				for (int d2 = 0; d2 < base; d2++) {
					for (int d3 = 0; d3 < base; d3++) {
						int number = d1 * base * base + d2 * base + d3;
						if (number % n != 0) {
							continue;
						}

						int sumDigits = d1 + d2 + d3;
						if (sumDigits % n != 0) {
							isRegularity = false;
							break;
						}
					}

					if (!isRegularity) break;
				}

				if (!isRegularity) break;
			}

			if (isRegularity) digits.push_back(n);
		}

		return digits;
	}
};

