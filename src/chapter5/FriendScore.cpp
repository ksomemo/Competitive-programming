#include <vector>
#include <string>
#include <algorithm>

class FriendScore {
public:
	int highestScore(std::vector <std::string> friends) {
		int highScore = 0;
		for (int i = 0; i < friends.size(); i++) {
			// 自分とは友人でないので、次の人から
			int score = 0;
			for (int j = i + 1; j < friends[i].length(); j++) {
				if (friends[i][j] == 'Y') score++;
			}

			highScore = std::max(highScore, score);
		}

		return highScore;
	}
};

