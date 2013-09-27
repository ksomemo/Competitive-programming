#include "chapter5/Cryptography.cpp"
#include "gtest/gtest.h"
#include <vector>

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

TEST_F(CryptographyTest, existsSameNumbers) {
	std::vector <int> numbers;
	numbers.push_back(1);
	numbers.push_back(3);
	numbers.push_back(2);
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(3);

	long actual = sut->encrypt(numbers);
	long expected = 36;

	EXPECT_EQ(actual, expected);
}

TEST_F(CryptographyTest, BigNumbersNoOverFlow) {
	std::vector <int> numbers;
	numbers.push_back(1000);
	numbers.push_back(999);
	numbers.push_back(998);
	numbers.push_back(997);
	numbers.push_back(996);
	numbers.push_back(995);

	long actual = sut->encrypt(numbers);
	long expected = 986074810223904000;

	EXPECT_EQ(actual, expected);
}

TEST_F(CryptographyTest, allSameNumbers) {
	std::vector <int> numbers;
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(1);

	long actual = sut->encrypt(numbers);
	long expected = 2;

	EXPECT_EQ(actual, expected);
}

