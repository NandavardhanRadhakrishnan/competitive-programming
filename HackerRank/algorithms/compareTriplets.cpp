 //https://www.hackerrank.com/challenges/compare-the-triplets/
 //compare two triplets and return a vector in which give points if a triplet is greater than the other, and 0 if equal

#include <bits/stdc.h>
using namespace std;

vector<int> compareTriplets(vector<int> a, vector<int> b) {
	int alice,bob=0;
	for(int i=0;i<3;i++){
		alice += a[i] > b[i];
		bob += b[i] > a[i];
	}
	vector<int> res = {alice,bob};
	return res;
}

int main(){
	vector<int> a = {5,6,7};
	vector<int> b = {3,6,10};
	vector<int> r = compareTriplets(a,b);
	for(auto x:r){cout<<x<<" ";};
}