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

	std::vector <int> digitsMySimple(int base) {
		std::vector <int> digits;

		int maxDigitOfNumber = 3;
		for (int n = 2; n < base; n++) {
			int num = 0;
			bool ok = true;
			while (true) {
				num++;
				// n倍判定
				if (num % n != 0){
					continue;
				}

				// 桁数を求める
				int divined = num;
				int sumDigits = 0;
				int digitOfNumber = 0;
				while (divined > 0) {
					if (digitOfNumber >= maxDigitOfNumber) {
						break;
					}

					sumDigits += divined % base;
					divined = divined / base;
					digitOfNumber++;
				}

				if (digitOfNumber >= maxDigitOfNumber) {
					break;
				}

				// 桁数の総和と倍数判定
				if (sumDigits % n != 0) {
					ok = false;
					break;
				}
			}

			if (ok) digits.push_back(n);
		}

		return digits;
	}
};

