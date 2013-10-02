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

