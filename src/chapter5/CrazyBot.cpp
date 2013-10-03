class CrazyBot {
public:
	double getProbability(int step, int east, int west, int south, int north) {
		if (step == 1) return 1.0;

		// 進む方角が直行している場合
		if (east == 100 || west == 100 || south == 100 || north == 100) return 1.0;

		if (east >  0 && west == 0 && south >  0 && north == 0) return 1.0;
		if (east == 0 && west >  0 && south >  0 && north == 0) return 1.0;
		if (east >  0 && west == 0 && south == 0 && north >  0) return 1.0;
		if (east == 0 && west >  0 && south == 0 && north >  0) return 1.0;

		double probability = 0.0;
		double pointProb[] = {east / 100.0, west / 100.0, south / 100.0, north / 100.0};
		int pointPetternCnt = sizeof(pointProb) / sizeof(pointProb[0]);
		for (int s1p = 0; s1p < pointPetternCnt; s1p++) {
			for (int s2p = 0; s2p < pointPetternCnt; s2p++) {
				if (s1p != s2p) {
					probability += pointProb[s1p] * pointProb[s2p];
				}
			}
		}

		return probability;
	}
};

