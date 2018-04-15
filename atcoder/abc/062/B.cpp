#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int H, W;
  cin >> H >> W;
  string a[H];
  REP(i, H) cin >> a[i];

  // C++17
  // string('#', W + 2) << endl;
  REP(i, W + 2) cout << '#';
  cout << endl;

  REP(i, H) {
    string line = "#" + a[i] + "#";
    cout << line << endl;
  }

  REP(i, W + 2) cout << '#';
  cout << endl;

  return 0;
}
