#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
using ll = long long;

int main() {
  int N;
  cin >> N;

  ll L[86 + 10];
  L[0] = 2, L[1] = 1;
  for (int i = 2; i <= N; i++) {
    L[i] = L[i - 1] + L[i - 2];
  }

  cout << L[N] << endl;

  return 0;
}
