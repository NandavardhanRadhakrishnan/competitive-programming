// https://www.hackerrank.com/challenges/organizing-containers-of-balls/
// given set of containers and balls of different color, return if you can organise them only by swapping

#include <bits/stdc.h>
using namespace std;

// we for swapping there is no change in no of balls in a container, so if there exist a contaier which has a size n, and color which has no of balls m, and n==m for all possible containers and colors then possible to swap else false

string organizingContainers(vector<vector<int>> container) {
	int n = container[0].size();
	vector<int> noOfBallsByColor(n);
	vector<int> noOfBallsByContainer(n);

	//container sum
	for (int i = 0; i < n; i++) {
		noOfBallsByContainer[i] = accumulate(container[i].begin(), container[i].end(), 0);
	}

	//color sum
	for (int i = 0; i < n; i++) {
		int t = 0;
		for (int j = 0; j < n; j++) {
			t += container[j][i];
		}
		noOfBallsByColor[i] += t;
	}

	sort(noOfBallsByColor.begin(), noOfBallsByColor.end());
	sort(noOfBallsByContainer.begin(), noOfBallsByContainer.end());

	if (noOfBallsByColor == noOfBallsByContainer) { return "Possible"; }

	return "Impossible";
}

int main() {
	vector<vector<int>> b = { {0,2,1},{1,1,1},{2,0,0} };
	cout<<organizingContainers(b);
	return 0;
}