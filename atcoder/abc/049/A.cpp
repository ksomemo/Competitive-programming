#include <bits/stdc++.h>
using namespace std;

int main() {
  char c;
  cin >> c;

  string s = "aiueo";
  // TODO: &
  for (auto &v : s) {
    if (c == v) {
      cout << "vowel" << endl;
      return 0;
    }
  }

  cout << "consonant" << endl;

  return 0;
}
