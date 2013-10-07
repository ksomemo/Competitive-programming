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
};

