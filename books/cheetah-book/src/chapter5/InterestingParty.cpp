#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

class InterestingParty {
public:
	int bestInvitation(vector <string> first, vector <string> second) {
		if (first.size() != second.size()) {
			throw "interesting count is invalid.";
		}

		map<string, int> sameInterestingCnts;
		for (int fi = 0; fi < first.size(); fi++) {
			if (sameInterestingCnts.find(first[fi]) != sameInterestingCnts.end()) {
				sameInterestingCnts[first[fi]] += 1;
			} else {
				sameInterestingCnts.insert(pair<string, int>(first[fi], 1));
			}
		}
		for (int si = 0; si < second.size(); si++) {
			if (sameInterestingCnts.find(second[si]) != sameInterestingCnts.end()) {
				sameInterestingCnts[second[si]] += 1;
			} else {
				sameInterestingCnts.insert(pair<string, int>(second[si], 1));
			}
		}

		int maxCnt = 1;
		map<string, int>::iterator it = sameInterestingCnts.begin();
		while (it != sameInterestingCnts.end()) {
			maxCnt = max(maxCnt, it->second);
			it++;
		}

		return maxCnt;
	}

	int bestInvitationVectorOnly(vector <string> first, vector <string> second) {
		int maxCnt = 0;

		for (int fi = 0; fi < first.size(); fi++) {
			int fCnt = 0;
			int sCnt = 0;
			for (int si = 0; si < first.size(); si++) {
				if ( first[fi] ==  first[si]) fCnt++;
				if ( first[fi] == second[si]) fCnt++;
				if (second[fi] ==  first[si]) sCnt++;
				if (second[fi] == second[si]) sCnt++;
			}

			maxCnt = max(fCnt, maxCnt);
			maxCnt = max(sCnt, maxCnt);
		}

		return maxCnt;
	}
};

