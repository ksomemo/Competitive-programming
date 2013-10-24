class SarumansArmy {
public:
	int markNum(int dotPos[], int dotNum, int interval) {
		int markNum = 0;
		int pos = 0;
		int markPos = 0;
		int movePos = 0;

		while (pos < dotNum) {
			// 印を付ける一番遠い位置を求める
			for (int i = pos; i < dotNum; i++) {
				if (dotPos[pos] + interval >= dotPos[i]) {
					markPos = i;
				} else {
					break;
				}
			}

			// 印を付ける位置の範囲外の点を求め、そこから上記の処理を繰り返す
			for (int i = markPos; i < dotNum; i++) {
				if (dotPos[markPos] + interval < dotPos[i]) {
					movePos = i;
					break;
				}
			}

			markNum++;
			// 移動する点がない場合、終了する
			if (pos == movePos) break;
			// 移動する
			pos = movePos;
		}

		return markNum;
	}
};

