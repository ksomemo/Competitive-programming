#include "chapter2/SarumansArmy.cpp"
#include "gtest/gtest.h"

class SarumansArmyTest : public ::testing::Test {
protected:
	SarumansArmy* sut;

	SarumansArmyTest() {
	}

	virtual ~SarumansArmyTest() {
	}

	virtual void SetUp() {
		sut = new SarumansArmy();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(SarumansArmyTest, testCaseName) {
	int dotPos[] = {1, 7, 15, 20, 30, 50};
	int dotNum = 6;
	int interval = 10;

	int actual = sut->markNum(dotPos, dotNum, interval);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}

