#include <bits/stdc++.h>
using namespace std;

int main() {
  string N;
  cin >> N;

  bool c1 = N[0] == N[1] && N[1] == N[2];
  bool c2 = N[1] == N[2] && N[2] == N[3];
  if (c1 || c2) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
