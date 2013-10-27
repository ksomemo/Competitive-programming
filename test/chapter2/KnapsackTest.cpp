#include "chapter2/KnapSack.cpp"
#include "gtest/gtest.h"

class KnapSackTest : public ::testing::Test {
protected:
	KnapSack* sut;

	KnapSackTest() {
	}

	virtual ~KnapSackTest() {
	}

	virtual void SetUp() {
		sut = new KnapSack();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(KnapSackTest, testCaseName) {
	int num = 4;
	int limit = 5;
	int weights[] = {2, 1, 3, 2};
	int values[] = {3, 2, 4, 2};

	int actual = sut->highestValue(num, limit, weights, values);
	int expected = 7;

	EXPECT_EQ(actual, expected);
}

