#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  int a[N];
  REP(i, N) cin >> a[i];

  sort(a, a + N, greater<int>());
  int ans, alice, bob;
  ans = alice = bob = 0;
  REP(i, N) {
    if (i % 2 == 0)
      alice += a[i];
    else
      bob += a[i];
  }
  ans = alice - bob;
  cout << ans << endl;

  return 0;
}
