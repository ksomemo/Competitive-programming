#include <vector>

class Cryptography {
public:
	long encrypt(std::vector <int> numbers) {
		int minPos = 0;
		for (int i = 0; i < numbers.size(); i++) {
			if (numbers[minPos] > numbers[i]) {
				minPos = i;
			}
		}

		numbers[minPos]++;

		long product = 1;
		for (int i = 0; i < numbers.size(); i++) {
			product *= numbers[i];
		}

		return product;
	}
};

