// ・sapmleTest.c
#include "gtest/gtest.h"
#include "sample.c"
 
//--------------------------------------------------
// pop2 test
//--------------------------------------------------
TEST(pop2, t0) { ASSERT_EQ(pop2(0), 0); }
TEST(pop2, t1) { ASSERT_EQ(pop2(1), 1); }
TEST(pop2, t2) { ASSERT_EQ(pop2(2), 1); }
TEST(pop2, t3) { ASSERT_EQ(pop2(3), 2); }
TEST(pop2, t4) { ASSERT_EQ(pop2(1023), 10); }
TEST(pop2, t5) { ASSERT_EQ(pop2(1024), 1); }
TEST(pop2, t6) { ASSERT_EQ(pop2(0xffff), 16); }
TEST(pop2, t7) { ASSERT_EQ(pop2(0x5555), 8); }
TEST(pop2, t8) { ASSERT_EQ(pop2(0xffffffff), 32); }
 
//--------------------------------------------------
// pop test
//--------------------------------------------------
TEST(pop, t0) { ASSERT_EQ(pop(0), 0); }
TEST(pop, t1) { ASSERT_EQ(pop(1), 1); }
TEST(pop, t2) { ASSERT_EQ(pop(2), 1); }
TEST(pop, t3) { ASSERT_EQ(pop(3), 2); }
TEST(pop, t4) { ASSERT_EQ(pop(1023), 10); }
TEST(pop, t5) { ASSERT_EQ(pop(1024), 1); }
TEST(pop, t6) { ASSERT_EQ(pop(0xffff), 16); }
TEST(pop, t7) { ASSERT_EQ(pop(0x5555), 8); }
TEST(pop, t8) { ASSERT_EQ(pop(0xffffffff), 32); }
