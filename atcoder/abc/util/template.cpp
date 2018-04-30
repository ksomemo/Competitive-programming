#include <bits/stdc++.h>
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define ALL(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;

template <typename T>
T proto_add(T a, T b);

template <>
int proto_add<int>(int a, int b) {
  // error: specialization of 'T proto_add(T, T) [with T = int]' after
  // instantiation
  // prototype宣言していても、引数intである呼び出しコードより先に書くこと
  int r = a + b;
  cout << r << endl;
  return r;
}

template <typename T, class C>
class MyClass {
 public:
  T v;
  C c;

 public:
  template <typename U>
  U id(U x) {
    // error: one liner
    return x;
  }
};

int main() {
  // template
  cout << "start" << endl;

  // error: invalid operands of types 'const char*' and 'const char*' to binary
  // 'operator+'
  // assert(proto_add("a", "b") == "ab");
  assert(proto_add<string>("a", "b") == "ab");
  assert(proto_add(1, 2) == 3);
  assert(proto_add(1.0, 3.0) == 4.0);

  cout << "end" << endl;
  return 0;
}

template <typename T>
T proto_add(T a, T b) {
  // error: one liner
  return a + b;
}
