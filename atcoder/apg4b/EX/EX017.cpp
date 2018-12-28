#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define REP(i, N) for (ll i = 0; i < (ll)(N); i++)
#define FOR(i, a, b) for (ll i = (a); i <= (ll)(b); i++)
#define ALL(x) (x).begin(), (x).end()

int main() {
  int N, S;
  cin >> N >> S;
  vector<int> A(N), P(N);
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }
  for (int i = 0; i < N; i++) {
    cin >> P.at(i);
  }

  // リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
  // ここにプログラムを追記
  int ans = 0;
  REP(i, N) {
    REP(j, N) {
      if (A[i] + P[j] == S) ans++;
    }
  }

  cout << ans << endl;
  return 0;
}
