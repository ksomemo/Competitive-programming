#include "chapter5/Cryptography.cpp"
#include "gtest/gtest.h"
#include <vector>
// using namespace std;

class CryptographyTest : public ::testing::Test {
protected:
	Cryptography *sut;

	CryptographyTest() {
	}

	virtual ~CryptographyTest() {
	}

	virtual void SetUp() {
		sut = new Cryptography();
	}

	virtual void TearDown() {
		delete sut;
	}
};

TEST_F(CryptographyTest, eachDiffrent) {
	std::vector <int> numbers;
	numbers.push_back(1);
	numbers.push_back(2);
	numbers.push_back(3);

	long actual = sut->encrypt(numbers);
	long expected = 12;

	EXPECT_EQ(actual, expected);
}

