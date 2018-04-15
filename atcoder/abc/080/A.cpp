#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int p1 = N * A;
  int ans = min(p1, B);

  cout << ans << endl;

  return 0;
}
