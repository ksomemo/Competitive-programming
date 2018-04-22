#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;

  set<tuple<int, int, int> > s;
  int ans = 0;
  FOR(i, 0, A) {
    FOR(j, 0, B) {
      FOR(k, 0, C) {
        int p = 500 * i + 100 * j + 50 * k;
        auto t = make_tuple(i, j, k);
        bool notFound = s.find(t) == s.end();
        if (p == X && notFound) ans++;
      }
    }
  }

  cout << ans << endl;

  return 0;
}
