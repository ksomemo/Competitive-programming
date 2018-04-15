#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  bool a = S[S.size() - 1] == 'T';
  string ans = a ? "YES" : "NO";
  cout << ans << endl;

  return 0;
}
