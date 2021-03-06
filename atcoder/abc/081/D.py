def main():
    """
    2<= N <= 50

    a_x += a_y: 2N回まで

    a_1 <= a_2 <= ... <= a_N にする
    """
    N = int(input())
    A = map(int, input().split())
    A = list(A)

    solve(N, A)


def solve(N, A):
    if A == sorted(A):
        print(0)
        return

    p = [i for i, a in enumerate(A) if a >= 0]
    m = [i for i, a in enumerate(A) if a < 0]

    # 調整
    operations = []
    plus = len(p) > 0
    if p and m:
        p_max_a = max(A[i] for i in p)
        m_min_a = min(A[i] for i in m)

        if abs(m_min_a) > abs(p_max_a):
            idx_list = p
            idx = A.index(m_min_a)
        else:
            idx_list = m
            idx = A.index(p_max_a)

        for i in idx_list:
            A[i] += A[idx]
            operations.append((idx+1, i+1))

    if sum(A) >= 0:
        for i in range(1, N):
            operations.append((i, i+1))
            A[i] += A[i-1]
    else:
        for i in range(N-1, 0, -1):
            operations.append((i+1, i))
            A[i-1] += A[i]

    print(len(operations))
    for src, dst in operations:
        print(src, dst)

    debug = False
    if debug:
        print(A)
        assert A == sorted(A)
        assert len(operations) <= N * 2


if __name__ == '__main__':
    main()


def dummy():
    """
    N<=50
    数列をソートする。ソートしても変わらないとき、操作0回
    2N以下の証明があるらしい→2Nより大きくなるときはどんなとき？
    N-1までソート済み、N個目は小さいとき、N-1を足す

    (案)
    ソートする・逆順ソートする
    足してみる・引いてみる、最大値との差分見てみる、累積和とってみる、前の項との差分見てみる

    数列は負も存在する
    なので、最大値を一番右に足して最大にしようとすると減少する場合がある
    そのときは、最小値を一番左に足して最小にする
    →最大値と最小値を確認する
    →左右その値が最小・最大なら操作必要なし

    ソートされているか確認しながらすすめる
    →右の値が大きいならOK
    →左の値が大きいなら調整
    →最大値が正の時、右に足す(なるべく足しすぎないように)
    →最大値が負の時、左すべてに足す
    →ソートされたので次の要素を確認
    →右に足すとき、足したためにその右より大きくなる可能性がある
    →左に足すとき、毎回左に足す、つまり逆順ソートされてるとき、毎回足さないといけない。N(N+1)/2 ？

    右が負の値で制約最小値であるとき、最大値を足してもまだ最大値にならないので、二回以上の操作が必要かもしれない

    操作をm=2N回以内に抑える必要があるので、-100から最大にするときを考えると、最大値が1であるとき最大値に最大値を足して2にしてからのほうが回数が少ない(そのまま:101回, 足してから:1+51)

    →ただし、負の値がないとき、増やした値は減らせないので、さらに最大値以上にする操作が必要になる可能性がある


    1234, 0000: sorted

    4321: N<=50なので、ソート済みからmaxになるように一回足す。maxを足す。
    →前項との差分作って、それを足す？差分が正なら調整不要

    432-1000: 負の数が強すぎる。正の数に負の数を足して対処

    432-1:負の数が弱い。累積和をとって、最後に調整？4798→479(17)
    →負の数のminと正の数のmaxそれぞれの絶対値のmaxが一番強い？

    43214321: 累積和とってみる。479(10)(14)(17)(19)(20)
    →大きい数だとオーバーフローしてだめ？
    →10^6,10^6-1,...,10^6-49、問題なさそう。負も(N<=50より)
    -4-3-2-14321: ソート済みの部分は累積和とらなくてよい。

    -1-2-3-4,4321: 負のソートされてない部分で累積和とるとNG。-1-3-6-10
    →逆順に累積和とる
    →-10-9-7-4,4321

    4321,-1-2-3-4,4321: 累積和・逆順累積和とる。479(10),-10-9-7-4,479(10)
    →左の正の区間・右の正の区間がソート済みにならない
    →正の区間は全て合わせて累積和とってみる
    →479(10),-10-9-7-4,(14)(17)(19)(20)
    →良さそう
    →間に挟まれた負の区間をどうする？
    →絶対値は20が最大なので、足してみる
    →479(10),(10)(11)(13)(16),(14)(17)(19)(20)
    →全てが正になったので、累積和とれば手順は満たすが回数は？
    →正: n, 負: m, 全体A=n+m, 正op: n-1(累積和), 負: m-1+m(逆順累積和+負から正) 全体累積和(n+m)
    →NG

    それよりも、全体を正負どちらかに寄せた後に累積和をとればよい
    →正負、それぞれの絶対値が多い方に寄せる(正maxを負に足す or 負minを正に足す)
    →その後累積和
    →寄せる(n or m)  + 累積和(n+m-1): OK
    """
