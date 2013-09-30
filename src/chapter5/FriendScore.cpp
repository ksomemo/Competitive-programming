#include <vector>
#include <string>
#include <algorithm>
#include <map>

class FriendScore {
public:
	int highestScore(std::vector <std::string> friends) {
		typedef std::vector <int> friendList;
		typedef std::vector<friendList> eachFriendList;

		// initialize
		eachFriendList eachFriends;
		for (int i = 0; i < friends.size(); i++) {
			friendList fl;
			eachFriends.push_back(fl);
		}

		for (int i = 0; i < friends.size(); i++) {
			for (int j = 0; j < friends[i].size(); j++) {
				if (i == j) continue;

				if (friends[i][j] == 'Y') {
					eachFriends[i].push_back(j);
				} else {
					for (int k = 0; k < friends[j].size(); k++) {
						if (friends[j][k] == 'Y' &&
							friends[k][i] == 'Y') {
							eachFriends[i].push_back(k);
						}
					}
				}
			}
		}

		int highScore = 0;
		for (int i = 0; i < eachFriends.size(); i++) {
			highScore = std::max(highScore, (int)eachFriends[i].size());
		}

		return highScore;
	}
};

