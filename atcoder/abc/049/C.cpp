#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  string S;
  cin >> S;

  string words[4] = {"dream", "dreamer", "erase", "eraser"};
  reverse(ALL(S));
  REP(i, 4) reverse(ALL(words[i]));

  int idx = 0;
  while (idx < S.size()) {
    bool match = false;
    for (const auto& w : words) {
      try {
        string sub = S.substr(idx, w.size());
        if (sub == w) {
          match = true;
          idx += w.size();
          break;
        }
      } catch (const out_of_range& e) {
        // 範囲のチェックではなく、例外を試すため
        cerr << "out_of_range: ";
        cerr << e.what() << endl;
      }
    }

    if (!match) {
      cout << "NO" << endl;
      return 0;
    }
  }
  cout << "YES" << endl;

  return 0;
}
