#include <bits/stdc++.h>
using namespace std;

int perm(int N, int i, int d, vector<int> types, int ans, vector<int> a) {
  if (i == d) {
    double x = 0;
    int c[7 + 1] = {0};

    bool non_zero = true;
    for (int i = 0; i < d; i++) {
      int v = a[i];
      x += v * pow(10, d - i - 1);
      if (non_zero && v != 0) non_zero = false;
      if (!non_zero) c[v]++;
    }
    /*
    // ref:
    https://beta.atcoder.jp/contests/dwacon5th-prelims/submissions/3655130 for
    (int i = 0; i < a.size(); i++) cout << a[i] << " "; cout << ", "; for (int i
    = 0; i <= 7; i++) cout << c[i] << " "; cout << ", " << x; cout << endl;
    */

    if (c[0] == 0 && c[7] >= 1 && c[5] >= 1 && c[3] >= 1 && x <= N) {
      ans++;
    }

    return ans;
  }

  for (auto t : types) {
    a[i] = t;
    ans = perm(N, i + 1, d, types, ans, a);
  }

  return ans;
}

int runPerm(int N, int d, vector<int> types) {
  auto a = vector<int>(d, 0);
  int ans = perm(N, 0, d, types, 0, a);
  return ans;
}

int main() {
  string S;
  cin >> S;
  int N = stoi(S);

  int d = S.size();
  vector<int> types = {0, 3, 5, 7};
  int ans = runPerm(N, d, types);
  cout << ans << endl;

  return 0;
}
