#include "chapter5/MazeMaker.cpp"
#include "gtest/gtest.h"
#include <string>
#include <vector>

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
	std::vector <std::string> maze;
	maze.push_back("...");
	maze.push_back("...");
	maze.push_back("...");

	int startRow = 0;
	int startCol = 1;
	int moveRowAr[] = {1, 0, -1, 0};
	int moveColAr[] = {0, 1, 0,  -1};
	std::vector<int> moveRow, moveCol;

	for (int i = 0; i < 4; i++) {
		moveRow.push_back(moveRowAr[i]);
		moveCol.push_back(moveColAr[i]);
	}

	int actual = sut->longestPath(maze, startRow, startCol, moveRow, moveCol);
	int expected = 3;

	EXPECT_EQ(actual, expected);
}

TEST_F(MazeMakerTest, _3x3MazeMoveToAround8DirectionOneStep) {
	std::vector <std::string> maze;
	maze.push_back("...");
	maze.push_back("...");
	maze.push_back("...");

	int startRow = 0;
	int startCol = 1;
	int moveRowAr[] = {1, 0, -1, 0,  1,  1, -1, -1};
	int moveColAr[] = {0, 1, 0,  -1, 1, -1,  1, -1};
	std::vector<int> moveRow, moveCol;

	for (int i = 0; i < 8; i++) {
		moveRow.push_back(moveRowAr[i]);
		moveCol.push_back(moveColAr[i]);
	}

	int actual = sut->longestPath(maze, startRow, startCol, moveRow, moveCol);
	int expected = 2;

	EXPECT_EQ(actual, expected);
}

