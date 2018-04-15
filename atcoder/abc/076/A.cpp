#include <bits/stdc++.h>
using namespace std;

int main() {
  int R, G;
  cin >> R >> G;

  // G = (R + ans) / 2;
  int ans = G * 2 - R;
  cout << ans << endl;

  return 0;
}
