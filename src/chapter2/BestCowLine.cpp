#include <string>
#include <iostream>

class BestCowLine {
public:
	std::string bestCowLine(std::string str) {
		std::string bestStr = "";
		int len = str.length();
		while (len > 0) {
			bool isSmallLeft = true;
			for (int i = 0; i < len / 2; i++) {
				if (str[i] < str[len - i - 1]) {
					break;
				} else if (str[i] > str[len - i - 1]) {
					isSmallLeft = false;
					break;
				}
			}

			if (len == 1) {
				bestStr += str[0];
				str = "";
			} else if (isSmallLeft) {
				bestStr += str[0];
				str = str.substr(1, len - 1);
			} else {
				bestStr += str[len - 1];
				str = str.substr(0, len - 1);
			}

			len = str.length();
		}

		return bestStr;
	}
};

