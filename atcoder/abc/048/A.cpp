#include <bits/stdc++.h>
using namespace std;

int main() {
  string s, ans;
  {
    string s1, s2;
    cin >> s1 >> s >> s2;
  }

  // empty
  // ans = "A" + s.at(0);
  ans = "A";
  ans += s.at(0);
  ans += "C";

  cout << ans << endl;

  return 0;
}
