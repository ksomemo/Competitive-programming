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

TEST_F(KiwiJuiceEasyTest, vector) {
	vector <int> vect1, vect2;
	vect1.push_back(1);
	vect1.push_back(2);
	vect2.push_back(1);
	vect2.push_back(2);
	
	EXPECT_EQ(vect1, vect2);
}

