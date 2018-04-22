#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N, Y;
  cin >> N >> Y;

  FOR(x, 0, N) {
    FOR(y, 0, N - x) {
      int z = N - x - y;
      int s = 10000 * x + 5000 * y + 1000 * z;
      if (s == Y) {
        cout << x << " " << y << " " << z << endl;
        return 0;
      }
    }
  }

  cout << "-1 -1 -1" << endl;

  return 0;
}
