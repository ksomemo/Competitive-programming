#include "chapter2/LakeCounting.cpp"
#include "gtest/gtest.h"

class LakeCountingTest : public ::testing::Test {
protected:
	LakeCounting* sut;

	LakeCountingTest() {
	}

	virtual ~LakeCountingTest() {
	}

	virtual void SetUp() {
		sut = new LakeCounting();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(LakeCountingTest, count3) {
	std::string area[] = {
		"W........WW.",
		".WWW.....WWW",
		"....WW...WW.",
		".........WW.",
		".........W..",
		"..W......W..",
		".W.W.....WW.",
		"W.W.W.....W.",
		".W.W......W.",
		"..W.......W.",
	};
	int col = area[0].length();
	int row = sizeof(area) / col;

	int actual = sut->lakeNum(area, col, row);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}
