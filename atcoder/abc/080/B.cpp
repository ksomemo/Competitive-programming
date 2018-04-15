#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int f(string X) {
  int s = 0;
  for (int i = 0; i < X.size(); i++) {
    s += X[i] - '0';
  }

  return s;
}

int main() {
  string N;
  cin >> N;
  int NX = stoi(N);
  int s = f(N);

  if (NX % s == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
