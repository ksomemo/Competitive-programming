#include <string>

class NumberMagicEasy {
public:
	int theNumber(std::string answer) {
		int minNumber = 1;
		int number = 0;
		int answerLen = answer.length();
		for (int i = 0; i < answerLen; i++) {
			if (answer[i] == 'N') {
				int add = 1;
				for (int j = 0; j < answerLen - i; j++) {
					if (j == 0) continue;
					add *= 2;
				}
				number += add;
			}
		}

		return number + minNumber;
	}

	int theNumberFromNums(std::string answer) {
		int a[] = {1, 2, 3, 4, 5, 6,  7,  8};
		int b[] = {1, 2, 3, 4, 9, 10, 11, 12};
		int c[] = {1, 2, 5, 6, 9, 10, 13, 14};
		int d[] = {1, 3, 5, 7, 9, 11, 13, 15};
		int maxNumber = 16;

		for (int i = 1; i <= maxNumber; i++) {
			if (this->inArray(a, i) != answer[0]) continue;
			if (this->inArray(b, i) != answer[1]) continue;
			if (this->inArray(c, i) != answer[2]) continue;
			if (this->inArray(d, i) != answer[3]) continue;

			return i;
		}

		return 0;
	}

	char inArray(int nums[], int num) {
		for (int i = 0; i < 8; i++) {
			if (num == nums[i]) return 'Y';
		}

		return 'N';
	}
};

