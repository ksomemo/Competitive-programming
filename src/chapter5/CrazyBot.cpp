class CrazyBot {
public:
	double getProbability(int step, int east, int west, int south, int north) {
		if (step == 1) return 1.0;

		int pointPetternCnt = 4;
		int success = 0;
		int failure = 0;
		for (int s1p = 0; s1p < pointPetternCnt - 1; s1p++) {
			for (int s2p = 0; s2p < pointPetternCnt - 1; s2p++) {
				if (s1p == s2p) {
					failure++;
				} else {
					success++;
				}
			}
		}

		return (double)success / (pointPetternCnt * 2);
	}
};

