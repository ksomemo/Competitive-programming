#include "chapter2/BestCowLine.cpp"
#include "gtest/gtest.h"
#include <string>

class BestCowLineTest : public ::testing::Test {
protected:
	BestCowLine* sut;

	BestCowLineTest() {
	}

	virtual ~BestCowLineTest() {
	}

	virtual void SetUp() {
		sut = new BestCowLine();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(BestCowLineTest, testCaseName) {
	std::string str = "ACDBCB";
	std::string actual = sut->bestCowLine(str);
	std::string expected = "ABCBCD";

	EXPECT_EQ(actual, expected);
}

