#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int main() {
  int N, K;
  cin >> N >> K;

  int ans = 1;
  REP(i, N) {
    int a = ans * 2;
    int b = ans + K;
    ans = min(a, b);
  }

  cout << ans << endl;

  return 0;
}
