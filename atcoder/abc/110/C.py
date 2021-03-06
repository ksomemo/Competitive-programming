import string
import pytest


def main():
    """
    英小文字のみからなる文字列 S, T
    文字列 Sに対して、次の操作を何度でも行うことができます。

    操作
        2つの異なる英小文字 c1, c2を選び、
        Sに含まれる全ての 
        c1 を c2に、
        c2 を c1に、置き換える

    0回以上操作を行って、S を Tに一致させられるか判定

    1 <= |S| = |T| <= 2 * 10^5
    """
    S = input()
    T = input()

    # ans = f(S, T)
    ans = editorial(S, T)
    print(ans)


@pytest.mark.randomize(S=str, T=str, ncalls=10,
                       min_length=10, max_length=10,
                       str_attrs=("ascii_lowercase",))
def test_f(S, T):
    """自作関数は嘘解法だった
    """
    assert f(S, T) == editorial(S, T)


def editorial(S, T):
    ss = [-1] * 26
    ts = [-1] * 26
    for c1, c2 in zip(S, T):
        a = ord(c1) - ord("a")
        b = ord(c2) - ord("a")

        if ss[a] != 1 or ts[b] != 1:
            if ss[a] != b or ts[b] != a:
                return "No"
        else:
            ss[a] = b
            ts[b] = a

    return "Yes"


def f(S, T):
    """
    26文字存在しないとき
    S: abc
    T: def
        a -> d にしたい
        dbc
        dはSに存在しないので好きに変えられる, でよいか

    S: abc
    T: ddf
        a -> d: dbc
        b -> d: dが存在する
        bを存在しないものに変える: dzc, 状況は変わらない
        a,b入れ替えても意味がない
        a->x, b->x and x->b: bxc, 状況は変わらない

        割当がかぶっていると無理っぽい

    仮に3文字しか種類がない
    S: abc
    T: cab
        c->a, a->c: cba
        b->a, a->b: cab
    """
    ds = {c: set() for c in string.ascii_lowercase}
    dt = {c: set() for c in string.ascii_lowercase}
    for c1, c2 in zip(S, T):
        ds[c2].add(c1)
        dt[c1].add(c2)

    for c in string.ascii_lowercase:
        if len(ds[c]) >= 2 or len(dt[c]) >= 2:
            return "No"

    return "Yes"


if __name__ == '__main__':
    main()
