#include <vector>

class Cryptography {
public:
	long encrypt(std::vector <int> numbers) {
		for (int i = 0; i < numbers.size(); i++) {
			if (numbers[i] == 1) {
				numbers[i]++;
				break;
			}
		}

		long product = 1;
		for (int i = 0; i < numbers.size(); i++) {
			product *= numbers[i];
		}

		return product;
	}
};

