#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
using ll = long long;

int main() {
  int A, B;
  cin >> A >> B;

  int ans = 0;
  FOR(i, A, B) {
    string str = to_string(i);
    // auto s = set<char>();
    // s.insert(str[i]);
    bool p = true;
    int len = str.size();
    for (int j = 0; j < len / 2; j++) {
      if (str[j] != str[len - j - 1]) {
        p = false;
        break;
      }
    }
    if (p) ans++;
  }

  cout << ans << endl;

  return 0;
}
