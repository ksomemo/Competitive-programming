class DrawingLots {
public:
	bool existsComb(int lots[], int lotsNum, int sum) {

		for (int a = 0; a < lotsNum; a++) {
			for (int b = 0; a < lotsNum; a++) {
				for (int c = 0; a < lotsNum; a++) {
					for (int d = 0; d < lotsNum; d++) {
						if (lots[a] + lots[b] + lots[c] + lots[d] == sum) {
							return true;
						}
					}
				}
			}
		}

		return false;
	}
};

