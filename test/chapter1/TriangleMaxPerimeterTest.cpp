#include "chapter1/TriangleMaxPerimeter.cpp"
#include "gtest/gtest.h"

class TriangleMaxPerimeterTest : public ::testing::Test {
protected:
	TriangleMaxPerimeter* sut;

	TriangleMaxPerimeterTest() {
	}

	virtual ~TriangleMaxPerimeterTest() {
	}

	virtual void SetUp() {
		sut = new TriangleMaxPerimeter();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(TriangleMaxPerimeterTest, validTriangle) {
	std::vector<int> sides;
	sides.push_back(2);
	sides.push_back(3);
	sides.push_back(4);
	sides.push_back(5);
	sides.push_back(10);

	std::vector<int> actual = sut->sidesMaximizedPerimeter(sides);
	std::vector<int> expected;
	expected.push_back(3);
	expected.push_back(4);
	expected.push_back(5);

	EXPECT_EQ(actual, expected);
}

