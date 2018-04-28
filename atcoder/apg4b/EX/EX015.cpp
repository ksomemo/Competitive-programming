#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

// 1人のテストの点数scoresから合計点を計算して返す関数
int sum(vector<int> scores) {
  // ここにプログラムを追記
  int s = 0;
  for (const auto &score : scores) {
    s += score;
  }
  return s;
}

// 3人の合計点からプレゼントの予算を計算して出力する関数
void output(int sum_a, int sum_b, int sum_c) {
  // ここにプログラムを追記
  int ans = sum_a * sum_b * sum_c;
  cout << ans << endl;
}

// -------------------
// ここから先は変更しない
// -------------------

// N個の入力を受け取って配列に入れて返す関数
vector<int> input(int N) {
  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }
  return vec;
}

int main() {
  // 科目の数Nを受け取る
  int N;
  cin >> N;

  // それぞれのテストの点数を受け取る
  vector<int> A, B, C;
  A = input(N);
  B = input(N);
  C = input(N);

  // プレゼントの予算を出力
  output(sum(A), sum(B), sum(C));
}
