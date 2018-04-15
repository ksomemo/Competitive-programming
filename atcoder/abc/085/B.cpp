#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  int d[N];
  REP(i, N) cin >> d[i];

  sort(d, d + N, greater<int>());
  int ans = 1;
  REP(i, N - 1) {
    if (d[i] > d[i + 1]) ans++;
  }

  cout << ans << endl;

  return 0;
}
