#include "chapter1/DrawingLots.cpp"
#include "gtest/gtest.h"

class DrawingLotsTest : public ::testing::Test {
protected:
	DrawingLots* sut;

	DrawingLotsTest() {
	}

	virtual ~DrawingLotsTest() {
	}

	virtual void SetUp() {
		sut = new DrawingLots();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(DrawingLotsTest, existsComb) {
	int lots[] = {1, 3, 5};
	int lotsNum = sizeof(lots) / sizeof(lots[0]);
	int sum = 10;

	bool actual = sut->existsComb(lots, lotsNum, sum);
	bool expected = true;

	EXPECT_EQ(actual, expected);
}

TEST_F(DrawingLotsTest, notExistsComb) {
	int lots[] = {1, 3, 5};
	int lotsNum = sizeof(lots) / sizeof(lots[0]);
	int sum = 9;

	bool actual = sut->existsComb(lots, lotsNum, sum);
	bool expected = false;

	EXPECT_EQ(actual, expected);
}

