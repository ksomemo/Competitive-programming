#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  int t[N], x[N], y[N];
  REP(i, N) cin >> t[i] >> x[i] >> y[i];

  int px = 0;
  int py = 0;
  int pt = 0;
  bool ok = true;
  REP(i, N) {
    int dt = t[i] - pt;
    int dx = abs(x[i] - px);
    int dy = abs(y[i] - py);

    if ((dt < dx + dy) || (dt - dx - dy) % 2 == 1) {
      ok = false;
      break;
    }

    pt = t[i];
    px = x[i];
    py = y[i];
  }

  if (ok) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
