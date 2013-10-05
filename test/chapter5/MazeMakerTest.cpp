#include "chapter5/MazeMaker.cpp"
#include "gtest/gtest.h"
#include <string>

class MazeMakerTest : public ::testing::Test {
protected:
	MazeMaker* sut;

	MazeMakerTest() {
	}

	virtual ~MazeMakerTest() {
	}

	virtual void SetUp() {
		sut = new MazeMaker();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(MazeMakerTest, _3x3MazeMoveToUpDownRightLeftOneStep) {
	std::string maze[] = {	"...",
							"...",
							"..."};

	int startRow = 0;
	int startCol = 1;
	int moveRow[] = {1, 0, -1, 0};
	int moveCol[] = {0, 1, 0,  -1};

	int actual = sut->longestPath(maze, startRow, startCol, moveRow, moveCol);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}

