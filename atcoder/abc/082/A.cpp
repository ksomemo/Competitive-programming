#include <bits/stdc++.h>
using namespace std;

int _ceil(int a, int b) {
  int x = (a + b - 1) / b;
  return x;
}

int main() {
  int a, b;
  cin >> a >> b;

  int ans = _ceil(a + b, 2);
  cout << ans << endl;

  return 0;
}

int solve(int a, int b) {
  double x = (a + b) / 2.0;
  int ans = (int)x;
  if (x > ans) {
    ans++;
  }

  return ans;
}
