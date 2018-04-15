#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N, M;
  cin >> N >> M;
  int a[M], b[M];
  REP(i, M) {
    cin >> a[i];
    cin >> b[i];
  }

  vector<int> ans(N, 0);
  REP(i, M) {
    ans[a[i] - 1]++;
    ans[b[i] - 1]++;
  }

  REP(i, N) cout << ans[i] << endl;

  return 0;
}
