import math


def main():
    """
       /|
    b / | h
     /  |
    /＿＿|＿_
    <- a -->

    底辺a, 斜辺b, aとbの間の角C(度)
    Cに対応するradianを求める

    もう1つの斜辺: x
    高さ: h (bを円の半径とした時、sinを利用して求める
    面積: S (自明)

    L (x + a + b): 三平方の定理を利用する
    x = sqrt(a_ ** 2 + h ** 2)
    図のaの右から垂線hまでの長さを a_ とすると
    a_ = a - b * cos(rad)
    ※ 余弦定理と三平方の定理 でググったほうがよい
    """
    a, b, C = map(int, input().split())

    # 三角形より、 0 < C < 180
    rad = math.pi * C / 180
    sin = math.sin(rad)
    h = b * sin
    S = a * h / 2

    a_ = a - b * math.cos(rad)
    len_d = math.sqrt(a_ ** 2 + h ** 2)
    # (a - b * cos)^ 2 + (b * sin)^2
    # a^2 -2ab * cos + b^2(cos)^2 + b^2(sin)^2
    # a^2 -2ab * cos + b^2

    print("{:.8f}".format(S))
    print("{:.8f}".format(a + b + len_d))
    print("{:.8f}".format(h))

if __name__ == "__main__":
    main()
