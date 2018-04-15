#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int main() {
  int H, W;
  cin >> H >> W;
  string s[H];
  REP(i, H) cin >> s[i];

  auto d = vector<tuple<int, int> >();
  // https://cpprefjp.github.io/lang/cpp11/range_based_for.html
  for (auto dx : {1, 0, -1}) {
    for (auto dy : {1, 0, -1}) {
      if (dx == 0 && dy == 0) continue;
      d.push_back(make_tuple(dx, dy));
    }
  }

  // print debug & unpack
  for (auto &t : d) {
    int dx, dy;
    std::tie(dx, dy) = t;
    // cout << dx << ',' << dy << endl;
  }

  char c[H][W];
  REP(i, H) {
    REP(j, W) {
      if (s[i][j] == '#') {
        c[i][j] = '#';
      } else {
        int b = 0;
        for (auto &_d : d) {
          int x = j + get<0>(_d), y = i + get<1>(_d);
          if (0 <= x && x < W && 0 <= y && y < H && s[y][x] == '#') b++;
        }
        c[i][j] = b + '0';
      }
    }
  }

  REP(i, H) {
    REP(j, W) cout << c[i][j];
    cout << endl;
  }

  return 0;
}
