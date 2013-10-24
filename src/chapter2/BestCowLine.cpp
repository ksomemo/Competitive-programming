#include <string>

class BestCowLine {
public:
	std::string bestCowLine(std::string str) {
		std::string bestStr = "";
		int len = str.length();
		int posL = 0;
		int posR = len - 1;

		while (posL <= posR) {
			bool isSmallLeft = true;
			for (int i = 0; posL + i <= posR - i; i++) {
				if (str[posL + i] < str[posR - i]) {
					break;
				} else if (str[posL + i] > str[posR - i]) {
					isSmallLeft = false;
					break;
				}
			}

			if (isSmallLeft) {
				bestStr += str[posL];
				posL++;
			} else {
				bestStr += str[posR];
				posR--;
			}
		}

		return bestStr;
	}
};

