// https://www.hackerrank.com/challenges/encryption/
// put text in a grid and print back the vertical columns

# include <bits/stdc.h>
using namespace std;

string encryption(string s) {
	s.erase(remove(s.begin(), s.end(), ' '), s.end());
	int r = floor(sqrt(s.length()));
	int c = ceil(sqrt(s.length()));
	if (r * c < s.length()) {
		r++;
	}
	string encrypted;
	for (int i = 0; i < c; i++) {
		for (int j = 0; j < r; j++) {
			int idx = i + (j * c);
			if (idx >= s.length()) {
				continue;
			}
			else {
				encrypted += s[idx];
			}
		}
		encrypted += ' ';
	}
	return encrypted;
}

int main() {
	string s = "if man was meant to Stay on the ground god wou1d have given us roots";
	cout<<encryption(s);
	return 0;
}