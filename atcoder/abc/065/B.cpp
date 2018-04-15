#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;
  int a[N];
  REP(i, N) cin >> a[i];

  // bool pushed[N];
  // => false初期化ではないので注意
  // https://cpplover.blogspot.jp/2010/09/blog-post_18.html
  int pushed[N] = {0};
  int ans = 0;
  int b = 0;
  // debug: 標準エラーへ
  REP(i, N) cerr << pushed[i] << endl;
  do {
    if (pushed[b] == 1) {
      ans = -1;
      break;
    }

    ans++;
    pushed[b] = 1;
    b = a[b] - 1;

  } while (b != 1);

  cout << ans << endl;

  return 0;
}
