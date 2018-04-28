#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  int A1[N], A2[N];

  REP(i, N) cin >> A1[i];
  REP(i, N) cin >> A2[i];

  int ans = 0;
  int sum_a1 = 0;
  REP(i, N) {
    sum_a1 += A1[i];
    int s = sum_a1;
    FOR(j, i, N - 1) s += A2[j];
    ans = max(ans, s);
  }

  cout << ans << endl;

  return 0;
}
