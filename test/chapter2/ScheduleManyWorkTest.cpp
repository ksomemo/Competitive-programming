#include "chapter2/scheduleManyWork.cpp"
#include "gtest/gtest.h"

class ScheduleManyWorkTest : public ::testing::Test {
protected:
	ScheduleManyWork* sut;

	ScheduleManyWorkTest() {
	}

	virtual ~ScheduleManyWorkTest() {
	}

	virtual void SetUp() {
		sut = new ScheduleManyWork();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(ScheduleManyWorkTest, scheduleManyWork) {
	int workCnt = 5;
	int timesStart[] = {1, 2, 4, 6, 8};
	int timesFinish[] = {3, 5, 7, 9, 10};

	int actual = sut->scheduleManyWork(workCnt, timesStart, timesFinish);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}

