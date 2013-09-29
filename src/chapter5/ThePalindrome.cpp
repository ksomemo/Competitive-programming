#include <string>

class ThePalindrome {
public:
	static const int posValid = -1;

	int find(std::string s) {
		bool isPalindrome = this->isPalindrome(s);
		int len = s.length();

		return isPalindrome ? len : len + 1;
	}

	bool isPalindrome(std::string s) {
		int pos = this->posIsNotPalindrome(s);

		return pos == posValid;
	}

	/**
	 * 回文になっていない開始位置を返す
	 * 回分である場合、-1を返す
	 */
	int posIsNotPalindrome(std::string s) {
		int len = s.length();
		for (int i = 0; i < len; i++) {
			if (s[i] != s[len - 1 - i]) {
				return i;
			}
		}

		return posValid;
	}

};

