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

	/**
	 * a * n^2 + b * n + c
	 * = a * n^2 + b * n + (a + b + c) -a -b
	 * = (a * n^2 -a) + (b * n - b) + (a + b + c)
	 * = a(n^2 - 1) + b(n - 1) + (a + b + c)
	 * = {a(n + 1) + b}(n - 1) + (a + b + c)
	 *
	 * 基数から1引いた数で第一項がわり切れるときに、
	 * 第二項も割り切れるならば、
	 * 第二項の因数は、基数から1引いた数の因数である
	 */
	std::vector <int> digitsSimple(int base) {
		std::vector <int> digits;

		for (int i = 2; i < base; i++) {
			if ( (base - 1) % i == 0) digits.push_back(i);
		}

		return digits;
	}
};

