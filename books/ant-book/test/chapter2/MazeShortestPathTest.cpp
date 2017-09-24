#include "chapter2/MazeShortestPath.cpp"
#include "gtest/gtest.h"

class MazeShortestPathTest : public ::testing::Test {
protected:
	MazeShortestPath* sut;

	MazeShortestPathTest() {
	}

	virtual ~MazeShortestPathTest() {
	}

	virtual void SetUp() {
		sut = new MazeShortestPath();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(MazeShortestPathTest, bfsShortestTurn) {
	std::string maze[] = {
		"#S######.#",
		"......#..#",
		".#.##.##.#",
		".#........",
		"##.##.####",
		"....#....#",
		".####.##.#", // ←本来は存在しない真ん中の通路を作成することで
		"....#.....", // 最短経路を作成した.
		".####.###.",
		"....#...G#"
	};

	int actual = sut->shortestTurn(maze);
	int expected = 16;

	EXPECT_EQ(actual, expected);
}
