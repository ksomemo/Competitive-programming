#include "chapter2/ChoiceCoin.cpp"
#include "gtest/gtest.h"

class ChoiceCoinTest : public ::testing::Test {
protected:
	ChoiceCoin* sut;

	ChoiceCoinTest() {
	}

	virtual ~ChoiceCoinTest() {
	}

	virtual void SetUp() {
		sut = new ChoiceCoin();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(ChoiceCoinTest, choiceFewCoins) {
	int charge = 620;
	int coinTypeNums = 6;
	int coinTypes[] = {1, 5, 10, 50, 100, 500};
	int coinNums[] = {3, 2, 1, 3, 0, 2};

	int actual = sut->choiceFewCoins(charge, coinTypeNums, coinTypes, coinNums);
	int expected = 6;

	EXPECT_EQ(actual, expected);
}
