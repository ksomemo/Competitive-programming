#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	vector<int> a;
	a.push_back(1);
	a.push_back(3);
	a.push_back(3);
	a.push_back(3);
	a.push_back(5);

	cout << "data: 1,3,3,3,5" << endl
		 << endl;
	cout << "lower_bound(3): " << *lower_bound(a.begin(), a.end(), 3) << endl;
	cout << "lower_bound(3): " << *upper_bound(a.begin(), a.end(), 3) << endl;
	cout << "lower_bound(4): " << *lower_bound(a.begin(), a.end(), 4) << endl;
	cout << "upper_bound(4): " << *upper_bound(a.begin(), a.end(), 4) << endl;

	return 0;
}
