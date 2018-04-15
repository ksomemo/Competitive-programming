#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;

int main() {
  int N;
  cin >> N;
  auto LR = vector<pair<int, int> >(N);

  for (int i = 0; i < N; i++) {
    int l, r;
    cin >> l >> r;
    auto p = make_pair(l, r);
    LR[i] = p;
  }

  int ans = 0;
  REP(i, N) {
    int l = LR[i].first;
    int r = LR[i].second;
    ans += r - l + 1;
  }

  cout << ans << endl;

  return 0;
}
