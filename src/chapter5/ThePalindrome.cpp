#include <string>

class ThePalindrome {
public:
	int find(std::string s) {
		bool isPalindrome = this->isPalindrome(s);
		int len = s.length();

		return isPalindrome ? len : len + 1;
	}

	bool isPalindrome(std::string s) {
		int len = s.length();
		for (int i = 0; i < len; i++) {
			if (s[i] != s[len - 1 - i]) {
				return false;
			}
		}

		return true;
	}
};

