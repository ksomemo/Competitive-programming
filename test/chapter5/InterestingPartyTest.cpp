#include <vector>
#include <string>
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

TEST_F(InterestingPartyTest, one) {
	vector <string> first, second;

	first.push_back("variety");
	first.push_back("diversity");
	first.push_back("loquacity");
	first.push_back("courtesy");
	second.push_back("talking");
	second.push_back("spearking");
	second.push_back("discussion");
	second.push_back("meeting");

	EXPECT_EQ(sut->bestInvitation(first, second), 1);
}


