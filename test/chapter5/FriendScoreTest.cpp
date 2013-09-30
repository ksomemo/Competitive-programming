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

