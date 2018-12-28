#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  vector<int> data(5);

  REP(i, 5) cin >> data.at(i);

  string ans = "NO";
  FOR(i, 1, 4) {
    if (data[i] == data[i - 1]) ans = "YES";
  }

  cout << ans << endl;

  return 0;
}
