#include <bits/stdc++.h>
using namespace std;

int main() {
  int ABC[3], K;
  cin >> ABC[0] >> ABC[1] >> ABC[2];
  cin >> K;

  sort(ABC, ABC + 3);
  for (int i = 0; i < K; i++) ABC[2] *= 2;
  int ans = ABC[0] + ABC[1] + ABC[2];
  cout << ans << endl;

  return 0;
}
