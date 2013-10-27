#include "chapter2/FenceRepair.cpp"
#include "gtest/gtest.h"

class FenceRepairTest : public ::testing::Test {
protected:
	FenceRepair* sut;

	FenceRepairTest() {
	}

	virtual ~FenceRepairTest() {
	}

	virtual void SetUp() {
		sut = new FenceRepair();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(FenceRepairTest, testCaseName) {
	int lenghs[] = {8, 5, 8};
	int lenNum = 3;

	int actual = sut->lowestCostCut(lenghs, lenNum);
	int expected = 34;

	EXPECT_EQ(actual, expected);
}

TEST_F(FenceRepairTest, testCaseName2) {
	int lenghs[] = {3, 4, 5, 1, 2};
	int lenNum = 5;

	int actual = sut->lowestCostCut(lenghs, lenNum);
	int expected = 33;

	EXPECT_EQ(actual, expected);
}

