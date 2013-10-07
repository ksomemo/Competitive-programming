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

