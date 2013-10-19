#include "chapter2/Factorial.cpp"
#include "gtest/gtest.h"

class FactorialTest : public ::testing::Test {
	protected:
		Factorial* sut;

		FactorialTest() {
		}

		virtual ~FactorialTest() {
		}

		virtual void SetUp() {
			sut = new Factorial();
		}

		virtual void TearDown() {
			delete sut;
		}
};

TEST_F(FactorialTest, Fact3Returns6) {
	int actual = sut->fact(3);
	int expected = 6;

	EXPECT_EQ(actual, expected);
}

TEST_F(FactorialTest, Fact4Returns24) {
	int actual = sut->fact(4);
	int expected = 24;

	EXPECT_EQ(actual, expected);
}

