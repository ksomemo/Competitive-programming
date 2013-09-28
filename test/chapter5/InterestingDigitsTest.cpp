#include "chapter5/InterestingDigits.cpp"
#include "gtest/gtest.h"
#include <vector>

class InterestingDigitsTest : public ::testing::Test {
protected:
	InterestingDigits *sut;

	InterestingDigitsTest() {
	}

	virtual ~InterestingDigitsTest() {
	}

	virtual void SetUp() {
		sut = new InterestingDigits();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(InterestingDigitsTest, base10) {
	int base = 10;
	std::vector <int> actual = sut->digits(base);
	std::vector <int> expected;
	expected.push_back(3);
	expected.push_back(9);

	EXPECT_EQ(actual, expected);
}

TEST_F(InterestingDigitsTest, base3) {
	int base = 3;
	std::vector <int> actual = sut->digits(base);
	std::vector <int> expected;
	expected.push_back(2);

	EXPECT_EQ(actual, expected);
}

