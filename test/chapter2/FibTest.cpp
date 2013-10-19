#include "chapter2/Fib.cpp"
#include "gtest/gtest.h"

class FibTest : public ::testing::Test {
protected:
	Fib* sut;

	FibTest() {
	}

	virtual ~FibTest() {
	}

	virtual void SetUp() {
		sut = new Fib();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(FibTest, fib4Return3) {

	int actual = sut->fibonacciNumber(4);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}

TEST_F(FibTest, fib10Return55) {

	int actual = sut->fibonacciNumber(10);
	int expected = 55;

	EXPECT_EQ(actual, expected);
}

