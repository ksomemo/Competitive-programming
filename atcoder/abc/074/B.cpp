#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int main() {
  int N, K;
  int x[N];
  cin >> N >> K;
  REP(i, N) cin >> x[i];

  int ans = 0;
  REP(i, N) {
    int m = min(x[i], abs(K - x[i]));
    ans += m * 2;
  }

  cout << ans << endl;

  return 0;
}
