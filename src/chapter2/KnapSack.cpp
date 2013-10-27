class KnapSack {
public:
	int *weights;
	int *values;
	int num;
	int limit;

	int highestValue(int num, int limit, int weights[], int values[]) {
		// すべての品物を使うか・使わないかを総当りで行う
		this->weights = weights;
		this->values = values;
		this->num = num;
		this->limit = limit;

		int tryCnt = 1;
		int totalVal = 0;
		int totalW = 0;

		return this->dfs(tryCnt, totalVal, totalW);
		// 品物を加えたとき、限界を超えない場合
		// 追加して、次の品物を加える・または加えなかったときの価値を求める
		//
		// 品物を加えたとき、限界を超える場合
		// 品物を加えず、次の品物を加える・または加えなかったときときの価値を求める
		//
		// 加える品物がなかった場合
		// 終了する
		//
		// 必要なもの
		// 加えた品物の数→加えたではなく、加えようと試みた数にしないと先に進まない
		// トータルの重さ
		// トータルの価値
		//
		// これより、次の価値を求めるなのでループまたは再帰になる。
		// ループの場合、加える・加えないの分岐ができない
		// →価値を求める処理を途中途中のループに実装すればいけるが、
		// 品物の数に依存する、つまりループ数＝品物の数になるので数が変わるとコードも変わる
		//
		// 再帰の場合、加える・加えないの分岐を関数呼び出しのパラメータとして表現できる
		// 終了条件をきちんと決めれば、品物の数に依存することはない！
		//
		return totalVal;
	}

	int dfs(int tryCnt, int totalVal, int totalW) {
		return 7;
	}
};

