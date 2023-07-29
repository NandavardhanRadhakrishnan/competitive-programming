//https://www.hackerrank.com/challenges/3d-surface-area
//find surface area for a 3d object with n number of 1x1x1 cube placed on a 2d surface which has n on each square


#include<bits/stdc.h>
using namespace std;

void PadWithZero(int rows, int cols, vector<vector<int>>& A)
{
	for (int i = 0; i < rows; i++) {
		A.at(i).insert(A[i].begin(), 0);
		A.at(i).insert(A[i].end(), 0);
	}
	vector<int> v(cols + 2, 0);
	A.insert(A.begin(), v);
	A.insert(A.end(), v);
}

int surfaceArea(vector<vector<int>> A) {
	int rows = A.size();
	int cols = A.at(0).size();

	PadWithZero(rows, cols, A);
	int sum = 0;
	for (int x = 0; x < A.size(); x++) {
		for (int y = 0; y < A[0].size(); y++) {
			if (y > cols || x > rows) {
				continue;
			}
			else {
				sum += abs(A[x][y] - A[x + 1][y]);
				sum += abs(A[x][y] - A[x][y + 1]);
			}
		}
	}
	sum += (rows * cols) * 2;
	return sum;
}

int main()
{
	vector<vector<int>> A = { {1,2,1},{3,2,2},{4,3,4} };
	cout << surfaceArea(A);
}
