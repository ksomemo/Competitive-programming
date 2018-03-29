#include <algorithm>
#include <chrono>
#include <ctime>
#include <iostream>
#include <vector>

#define all(x) (x).begin(), (x).end()
using namespace std;
using ll = long long;
using ull = unsigned long long;

// https://gist.github.com/yosupo06/f8b62b4d070275d9814ecaf45519f720
//  g++-5 -W -std=c++14 0670.cpp
ull seed;
int next() {
  seed = seed ^ (seed << 13);
  seed = seed ^ (seed >> 7);
  seed = seed ^ (seed << 17);
  return (seed >> 33);
}

void TLE2(int n, int q, vector<int> a) {
  ll sm = 0;
  sort(all(a));

  for (int i = 0; i < q; i++) {
    int x = next();
    int cnt = lower_bound(all(a), x) - a.begin();
    sm ^= ll(cnt) * i;
  }
  cout << sm << endl;
}

void TLE(int n, int q, vector<int> a) {
  ll sm = 0;
  for (int i = 0; i < q; i++) {
    int x = next();
    int cnt = 0;
    for (int j = 0; j < n; j++) {
      if (a[j] < x) cnt++;
    }
    sm ^= ll(cnt) * i;
  }
  cout << sm << endl;
}

/**
 * TLEのボトルネック探しのために時間系ライブラリを探した
 *
 * https://cpprefjp.github.io/reference/chrono/system_clock/now.html
 * http://en.cppreference.com/w/cpp/chrono
 * http://ja.cppreference.com/w/cpp/chrono
 * https://yohe.gitbooks.io/cpp-14/content/chapter_1/library/chrono.html
 *
 * 解説
 *   https://yukicoder.me/problems/no/670/editorial
 *
 *   想定TLE解 O(NlogN+QlogN)
 *   最初に数列をsortするとクエリにO(logN)で答えられます。
 *   C++だと驚愕の6200ms、TLEが鬼になりました。
 *   想定解 O(NlogN+Q)
 *   クエリに定数時間で答えます。
 *   数列の値は[0,231)の区間に割りと一様分布することが期待できます
 *     (xorshiftは強いので)
 *   ここで、この区間をN個に分割し、それぞれの区間にいくつ要素があるか数えておきます。
 *   すると、クエリの値と同じ区間の要素だけ見れば良くて、期待値は1個です。
 *   実際には300,000個ぐらいに分割するのが一番速かったです
 *   (追記) なんかプロの提出を見てるともっと大きいほうが速そうでした
 *   (あとバケットサイズを2冪にするのも効果がある？)
 *
 * ニコ生コメント
 *   Eは基数ソートでゴリ押した
 *   Eはハッシュテーブルとかの原理だよね
 *   Ｅ、乱数の一様性利用しないと無理なのかな
 */
int main() {
  int n, q;
  cin >> n >> q >> seed;

  chrono::system_clock::time_point t1 = chrono::system_clock::now();
  for (int i = 0; i < 10000; i++) next();
  auto t2 = chrono::system_clock::now();
  chrono::system_clock::duration elapsed1 = t2 - t1;

  vector<int> a(n);
  for (int i = 0; i < n; i++) a[i] = next();
  auto t3 = chrono::system_clock::now();
  chrono::system_clock::duration elapsed2 = t3 - t2;

  time_t start_time = std::chrono::system_clock::to_time_t(t1);
  time_t finish_time = std::chrono::system_clock::to_time_t(t3);
  cout << "started at: " << ctime(&start_time) << endl;
  cout << elapsed1.count() << endl;
  cout << elapsed2.count() << endl;
  cout << "finished at: " << ctime(&finish_time) << endl;

  TLE2(n, q, a);
  // TLE(n, q, a);
  return 0;
}