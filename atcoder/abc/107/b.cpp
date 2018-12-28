#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define REP(i, N) for (ll i = 0; i < (ll)(N); i++)
#define FOR(i, a, b) for (ll i = (a); i <= (ll)(b); i++)
#define ALL(x) (x).begin(), (x).end()

int main() {
  int H, W;
  cin >> H >> W;
  string lines[H];
  REP(i, H) cin >> lines[i];

  bool ignore_row[H] = {false};
  bool ignore_col[W] = {false};
  REP(h, H) {
    int d = count(ALL(lines[h]), '.');
    if (d == W) ignore_row[h] = true;
  }

  REP(w, W) {
    int d = 0;
    REP(h, H) {
      if (lines[h][w] == '.') d++;
      if (d == H) ignore_col[w] = true;
    }
  }

  REP(h, H) {
    if (ignore_row[h]) continue;
    REP(w, W) {
      if (!ignore_col[w]) cout << lines[h][w];
    }
    cout << endl;
  }

  return 0;
}
