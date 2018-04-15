#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  // ここにプログラムを追記
  int ans = 1;
  for (int i = 1; i < S.size(); i++) {
    char c = S.at(i);
    if (c == '+') {
      ans++;
    } else if (c == '-') {
      ans--;
    }
  }

  cout << ans << endl;

  return 0;
}
