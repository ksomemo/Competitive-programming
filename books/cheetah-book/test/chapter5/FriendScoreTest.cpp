#include "chapter5/FriendScore.cpp"
#include "gtest/gtest.h"
#include <vector>
#include <string>

class FriendScoreTest : public ::testing::Test {
protected:
	FriendScore* sut;

	FriendScoreTest() {
	}

	virtual ~FriendScoreTest() {
	}

	virtual void SetUp() {
		sut = new FriendScore();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(FriendScoreTest, noFriend) {
	std::vector <std::string> friends;
	friends.push_back("NNN");
	friends.push_back("NNN");
	friends.push_back("NNN");

	int actual = sut->highestScore(friends);
	int expected = 0;

	EXPECT_EQ(actual, expected);
}

TEST_F(FriendScoreTest, noExsitsFriendFriend) {
	std::vector <std::string> friends;
	friends.push_back("NYNN");
	friends.push_back("YNNN");
	friends.push_back("NNNY");
	friends.push_back("NNYN");

	int actual = sut->highestScore(friends);
	int expected = 1;

	EXPECT_EQ(actual, expected);
}

TEST_F(FriendScoreTest, allFriend) {
	std::vector <std::string> friends;
	friends.push_back("NYY");
	friends.push_back("YNY");
	friends.push_back("YYN");

	int actual = sut->highestScore(friends);
	int expected = 2;

	EXPECT_EQ(actual, expected);
}

TEST_F(FriendScoreTest, exsitsFriendFriend) {
	std::vector <std::string> friends;
	friends.push_back("NYNNN"); // 1, |2
	friends.push_back("YNYNN"); // 0,2|3
	friends.push_back("NYNYN"); // 1,3|2,4
	friends.push_back("NNYNY"); // 2,4|1
	friends.push_back("NNNYN"); // 3  |2

	int actual = sut->highestScore(friends);
	int expected = 4;

	EXPECT_EQ(actual, expected);
}

