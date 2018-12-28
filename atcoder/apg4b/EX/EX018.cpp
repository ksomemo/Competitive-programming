#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define REP(i, N) for (ll i = 0; i < (ll)(N); i++)
#define FOR(i, a, b) for (ll i = (a); i <= (ll)(b); i++)
#define ALL(x) (x).begin(), (x).end()

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }

  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
  string r[N];
  REP(i, N) r[i] = string(N, '-');
  REP(i, M) {
    int w = A[i] - 1;
    int l = B[i] - 1;
    r[w][l] = 'o';
    r[l][w] = 'x';
  }

  REP(i, N) {
    REP(j, N) {
      cout << r[i][j];
      if (j != N - 1) {
        cout << ' ';
      } else {
        cout << endl;
      }
    }
  }

  return 0;
}
