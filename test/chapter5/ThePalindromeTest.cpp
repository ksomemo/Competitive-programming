#include "chapter5/ThePalindrome.cpp"
#include "gtest/gtest.h"
#include <string>

class ThePalindromeTest : public ::testing::Test {
protected:
	ThePalindrome* sut;

	ThePalindromeTest() {
	}

	virtual ~ThePalindromeTest() {
	}

	virtual void SetUp() {
		sut = new ThePalindrome();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(ThePalindromeTest, isPalindrome) {
	std::string s("abacaba");

	int actual = sut->find(s);
	int expected = 7;

	EXPECT_EQ(actual, expected);
}

