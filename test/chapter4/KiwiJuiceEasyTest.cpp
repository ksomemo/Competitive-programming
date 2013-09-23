#include "chapter4/KiwiJuiceEasy.cpp"
#include "gtest/gtest.h"

class KiwiJuiceEasyTest : public ::testing::Test {
protected:
	KiwiJuiceEasyTest() {
	}
	virtual ~KiwiJuiceEasyTest() {
	}
	virtual void SetUp() {
	}
	virtual void TearDown() {
	}
};

TEST_F(KiwiJuiceEasyTest, sample) {
	EXPECT_EQ("Fizz", "Fizz");
}

TEST_F(KiwiJuiceEasyTest, toOver) {
	vector <int> capacities, bottles, fromId, toId;
	capacities.push_back(10);
	capacities.push_back(10);

	bottles.push_back(5);
	bottles.push_back(8);

	fromId.push_back(0);

	toId.push_back(1);

	vector <int> expected, actual;
	KiwiJuiceEasy *sut;
	sut = new KiwiJuiceEasy();

	expected.push_back(3);
	expected.push_back(10);
	actual = sut->thePouring(capacities, bottles, fromId, toId);
	delete sut;

	EXPECT_EQ(expected, actual);
}

TEST_F(KiwiJuiceEasyTest, toUnfulfilled) {
	vector <int> capacities, bottles, fromId, toId;
	capacities.push_back(20);
	capacities.push_back(20);

	bottles.push_back(5);
	bottles.push_back(8);

	fromId.push_back(0);

	toId.push_back(1);

	vector <int> expected, actual;
	KiwiJuiceEasy *sut;
	sut = new KiwiJuiceEasy();

	expected.push_back(0);
	expected.push_back(13);
	actual = sut->thePouring(capacities, bottles, fromId, toId);
	delete sut;

	EXPECT_EQ(expected, actual);
}

