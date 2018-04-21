#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  int a[3] = {A, B, C};
  sort(a, a + 3);

  int ans = a[2] - a[0];
  cout << ans << endl;
  return 0;
}
