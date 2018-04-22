#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int ans = 0;
  FOR(i, 1, N) {
    int d = i;
    int s = 0;
    while (d >= 1) {
      s += d % 10;
      d = d / 10;
    }
    if (A <= s && s <= B) ans += i;
  }
  cout << ans << endl;

  return 0;
}
