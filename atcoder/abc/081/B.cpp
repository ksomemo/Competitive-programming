#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;

  int A[N];
  REP(i, N) cin >> A[i];

  int ans = 0;
  while (true) {
    bool even = true;
    REP(i, N) {
      if (A[i] % 2 == 1) {
        even = false;
        break;
      }
      A[i] /= 2;
    }
    if (even)
      ans++;
    else
      break;
  }

  cout << ans << endl;

  return 0;
}
