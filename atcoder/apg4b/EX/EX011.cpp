#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  // ここにプログラムを追記
  string ops[7];
  int bs[7];
  for (int i = 0; i < N; i++) {
    cin >> ops[i] >> bs[i];
  }

  int acc = A;
  for (int i = 1; i <= N; i++) {
    string op = ops[i - 1];
    int B = bs[i - 1];

    if (op == "+") {
      acc += B;
    } else if (op == "-") {
      acc -= B;
    } else if (op == "*") {
      acc *= B;
    } else if (B != 0) {
      acc /= B;
    } else {
      cout << "error" << endl;
      break;
    }

    cout << i << ":" << acc << endl;
  }

  return 0;
}
