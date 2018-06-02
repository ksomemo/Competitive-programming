#include <bits/stdc++.h>
#define REP(i, N) for (ll i = 0; i < (N); i++)
#define FOR(i, a, b) for (ll i = (a); i <= (b); i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

ll bin_search(const ll N, ll A[]) {
  const ll N_BIT = 20;
  ll b[N_BIT][N + 1];
  // bitごとの累積和
  REP(j, N_BIT) REP(i, N + 1) b[j][i] = 0;
  REP(j, N_BIT) {
    REP(i, N) {
      ll x = (A[i] >> j) & 1;
      b[j][i + 1] = x + b[j][i];
    }
  }

  ll INF = 1 << 30;
  ll ans = 0;
  REP(i, N) {
    ll tmp = INF;
    REP(j, N_BIT) {
      // 累積和の調整
      // i = 1のとき i = 0まで累積和 + 1がi = 1以降では許容される
      ll a = 1 + b[j][i];
      // 0 to N - 1ではなく、0 to Nなので - 1 と i + 1以降なので - i
      ll x = upper_bound(b[j], b[j] + N + 1, a) - b[j];
      tmp = min(tmp, x - 1 - i);
    }
    ans += tmp;
  }
  return ans;
}

int main() {
  ll N;
  cin >> N;
  ll A[N];
  REP(i, N) cin >> A[i];

  ll ans = bin_search(N, A);
  cout << ans << endl;

  return 0;
}
