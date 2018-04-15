#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
using ll = long long;

int main() {
  int N, M;
  cin >> N;
  string s[N];
  REP(i, N) cin >> s[i];
  cin >> M;
  string t[M];
  REP(i, M) cin >> t[i];

  map<string, int> m;
  REP(i, N) m[s[i]] += 1;
  REP(i, M) m[t[i]] -= 1;

  int ans = 0;
  for (auto &p : m) {
    // cerr << p.first << ":" << p.second << endl;
    ans = max(p.second, ans);
  }
  cout << ans << endl;

  return 0;
}
