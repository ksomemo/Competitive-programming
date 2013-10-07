#include "chapter5/NumberMagicEasy.cpp"
#include "gtest/gtest.h"
#include <string>

class NumberMagicEasyTest : public ::testing::Test {
protected:
	NumberMagicEasy* sut;

	NumberMagicEasyTest() {
	}

	virtual ~NumberMagicEasyTest() {
	}

	virtual void SetUp() {
		sut = new NumberMagicEasy();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(NumberMagicEasyTest, YesNoNoNoReturn8) {
	std::string answer = "YNNN";

	int actual = sut->theNumber(answer);
	int expected = 8;

	EXPECT_EQ(actual, expected);
}

TEST_F(NumberMagicEasyTest, ForthNoReturn16) {
	std::string answer = "NNNN";

	int actual = sut->theNumber(answer);
	int expected = 16;

	EXPECT_EQ(actual, expected);
}

TEST_F(NumberMagicEasyTest, ForthYesReturn1) {
	std::string answer = "YYYY";

	int actual = sut->theNumber(answer);
	int expected = 1;

	EXPECT_EQ(actual, expected);
}

TEST_F(NumberMagicEasyTest, NoYesNoYesReturn11) {
	std::string answer = "NYNY";

	int actual = sut->theNumber(answer);
	int expected = 11;

	EXPECT_EQ(actual, expected);
}

