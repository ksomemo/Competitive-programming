#include "chapter5/CrazyBot.cpp"
#include "gtest/gtest.h"

class CrazyBotTest : public ::testing::Test {
protected:
	CrazyBot* sut;

	CrazyBotTest() {
	}

	virtual ~CrazyBotTest() {
	}

	virtual void SetUp() {
		sut = new CrazyBot();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(CrazyBotTest, OneStep) {
	double actual = sut->getProbability(1, 25, 25, 25, 25);
	double expected = 1.0;
	EXPECT_EQ(actual, expected);
}

TEST_F(CrazyBotTest, twoStepAllCompassPoint) {
	double actual = sut->getProbability(2, 25, 25, 25, 25);
	double expected = 0.75;
	EXPECT_EQ(actual, expected);
}

TEST_F(CrazyBotTest, sevenStepNoCross) {
	double actual1 = sut->getProbability(7, 50, 0,  0,  50);
	double actual2 = sut->getProbability(7, 0,  50, 0,  50);
	double actual3 = sut->getProbability(7, 50, 0,  50, 0);
	double actual4 = sut->getProbability(7, 0,  50, 50, 0);

	double actual5 = sut->getProbability(7, 100, 0,   0,   0);
	double actual6 = sut->getProbability(7, 0,   100, 0,   0);
	double actual7 = sut->getProbability(7, 0,   0,   100, 0);
	double actual8 = sut->getProbability(7, 0,   0,   0,   100);

	double expected = 1.0;

	EXPECT_EQ(actual1, expected);
	EXPECT_EQ(actual2, expected);
	EXPECT_EQ(actual3, expected);
	EXPECT_EQ(actual4, expected);
	EXPECT_EQ(actual5, expected);
	EXPECT_EQ(actual6, expected);
	EXPECT_EQ(actual7, expected);
	EXPECT_EQ(actual8, expected);
}

