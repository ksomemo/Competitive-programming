#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define rep(i, a, b) for (int i = a; i < b; i++)
#define all(x) (x).begin(), (x).end()
// typedef long long ll;
using ll = long long;

const int N_MAX = 200000;
int A[N_MAX];
int B[N_MAX];

int editorial(int N) {
  int ans = 0;
  const int n_bit = 29;

  rep(i, 0, n_bit) {
    int t = 1 << i;
    int t2 = t << 1;

    vector<int> mod;
    rep(i, 0, N) {
      int b = B[i];
      mod.push_back(b & (t2 - 1));
    }
    sort(all(mod));

    auto count = 0;
    rep(i, 0, N) {
      int da = A[i] % t2;
      // iterator を返す
      int t1_count = lower_bound(all(mod), t - da) - mod.begin();
      int t2_count = lower_bound(all(mod), t2 - da) - mod.begin();
      int t3_count = lower_bound(all(mod), t * 3 - da) - mod.begin();

      count += N - t3_count + t2_count - t1_count;
    }

    if (count & 1 == 1) {
      ans += 1 << i;
    }
  }
  return ans;
}

int main() {
  int N, ans;
  cin >> N;

  rep(i, 0, N) cin >> A[i];
  rep(i, 0, N) cin >> B[i];

  ans = editorial(N);
  cout << ans << endl;

  return 0;
}
