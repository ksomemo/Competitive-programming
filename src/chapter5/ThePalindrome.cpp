#include <string>

class ThePalindrome {
public:
	int find(std::string s) {
		bool isPalindrome = true;
		int len = s.length();
		for (int i = 0; i < len; i++) {
			if (s[i] != s[len - 1 - i]) {
				isPalindrome = false;
				break;
			}
		}

		return isPalindrome ? len : len + 1;
	}
};

