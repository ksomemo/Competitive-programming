import math


def main():
    """
    H * W 板チョコ3分割
    面積：A B C
    minimize(max(A B C) - min(A B C))

    縦or横がMAX、片方が途中まで
    上記1つと、残りを半分
    残り：面積２以上
    """
    H, W = list(map(int, input().strip().split()))
    # 縦MAX, H>=2より、W-1まで確認
    # 横MAX, H>=2より、W=1のとき３分割できないので、W>=2
    answer = calc_answer(H, W)
    answer = calc_answer(W, H, answer=answer)
    print(answer)


def calc_answer(H, W, answer=None):
    # 縦MAX, H>=2より、W-1まで確認
    if answer is None:
        answer = float("inf")

    for _w in range(1, W):
        # 縦MAXで試す
        S = [
            H * _w,
            H * math.ceil((W - _w) / 2),
            H * int((W - _w) // 2),
        ]
        if not 0 in S:
            S_diff = max(S) - min(S)
            #print(H, _w, S, S_diff, answer, sep="\t")
            answer = min(answer, S_diff)

        # 横MAXで縦分割
        for _h in range(1, H):
            S = [
                H * _w,
                (W - _w) * _h,
                (W - _w) * (H - _h),
            ]
            if not 0 in S:
                S_diff = max(S) - min(S)
                #print(_h, _w, S, S_diff, answer, sep="\t")
                answer = min(answer, S_diff)

    return answer

if __name__ == '__main__':
    main()
