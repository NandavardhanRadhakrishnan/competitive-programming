// https://www.hackerrank.com/challenges/diagonal-difference/
// find difference of sum of diagonals in a matrix

#include <bits/stdc.h>
using namespace std;

int diagonalDifference(vector<vector<int>> arr) {
	int n = arr[0].size();
	int primaryD = 0;
	int secondaryD = 0;
	for (int i = 0; i < n; i++) {
		primaryD+=arr[i][i];
		secondaryD += arr[n - i - 1][i];
	}
	return abs(primaryD-secondaryD);
}

int main() {
	vector<vector<int>> v = { {11,2,4},{4,5,6},{10,8,-12} };
	cout<<diagonalDifference(v);
}