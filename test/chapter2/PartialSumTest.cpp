#include "chapter2/PartialSum.cpp"
#include "gtest/gtest.h"

class PartialSumTest : public ::testing::Test {
	protected:
		PartialSum* sut;

		PartialSumTest() {
		}

		virtual ~PartialSumTest() {
		}

		virtual void SetUp() {
			sut = new PartialSum();
		}

		virtual void TearDown() {
			delete sut;
		}
};

TEST_F(PartialSumTest, exists) {
	int nums[] = {1, 2, 4, 7};
	int numCnt = 4;
	int target = 13;

	bool actual = sut->exists(nums, numCnt, target);
	bool expected = true;

	EXPECT_EQ(actual, expected);
}

