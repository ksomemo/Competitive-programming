#include <vector>
#include "gtest/gtest.h"
#include "chapter5/InterestingParty.cpp"

class InterestingPartyTest : public ::testing::Test {
protected:
	InterestingParty *sut;

	InterestingPartyTest() {
	}

	virtual ~InterestingPartyTest() {
	}

	virtual void SetUp() {
		sut = new InterestingParty();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(InterestingPartyTest, all) {
	vector <string> first, second;

	first.push_back("fishing");
	first.push_back("gardening");
	first.push_back("swimming");
	first.push_back("fishing");
	second.push_back("hunting");
	second.push_back("fishing");
	second.push_back("fishing");
	second.push_back("biting");

	EXPECT_EQ(sut->bestInvitation(first, second), 4);
}

