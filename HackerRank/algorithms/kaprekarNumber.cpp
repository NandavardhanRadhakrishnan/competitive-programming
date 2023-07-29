// https://www.hackerrank.com/challenges/kaprekar-numbers
// given ints p and q find all kaprekar numbers from p to q

#include <bits/stdc.h>
using namespace std;

bool isKaprekar(int n) {
	
	if (n == 1) {
		return 1;
	}

	string s = to_string(n * n);
	int len = s.size();
	int d = floor(len / 2);

	if (len >= 2) {
		int l = stoi(s.substr(0, d));
		int r = stoi(s.substr(d));
		return (n == l + r);
	}
	return 0;
}

void kaprekarNumbers(int p, int q) {
	for (int i = p; i < q; i++) {
		if (isKaprekar(i) == 1) {
			cout << i << " ";
		}
	}
}

int main() {
	kaprekarNumbers(1,700);
	return 0;
}