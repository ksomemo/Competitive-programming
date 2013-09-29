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
	std::string sShort("aba");

	int actual = sut->find(s);
	int expected = 7;

	EXPECT_EQ(actual, expected);
	EXPECT_EQ(sut->find(sShort), 3);

	EXPECT_EQ(sut->findSampleBook(s),      expected);
	EXPECT_EQ(sut->findSampleBook(sShort), 3);
}

TEST_F(ThePalindromeTest, isNotPalindrome) {
	std::string s = "abab";

	int actual = sut->find(s);
	int expected = 5;

	EXPECT_EQ(actual, expected);
	EXPECT_EQ(sut->findSampleBook(s), expected);
}

