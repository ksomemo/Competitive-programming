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

	int findSampleBook(std::string s) {
		int len = s.size();
		int maxLen = len + (len - 1);

		for (int i = len; i < maxLen; i++) {
			bool sameChar = true;
			for (int j = 0; j < len; j++) {
				int posOtherSide = i - j -1;
				if (posOtherSide < len && s[j] != s[posOtherSide]) {
					sameChar = false;
					break;
				}
			}

			if (sameChar) return i;
		}

		return maxLen;
	}

	std::string makePalindrome(std::string s) {
		int len = s.length();
		int palindromeLen = find(s);

		if (len == palindromeLen) return s;

		std::string palindrome = "" + s;
		int addLen = palindromeLen - len;
		for (int i = addLen; i > 0; i--) {
			// stringがイミュータブルなのかわかってない
			palindrome += s[i - 1];
		}

		return palindrome;
	}
};

